---
type: guide
title: RustFS 模型公共读
tags: [deploy, rustfs]
created: 2026-10-24
updated: 2026-10-24
---

# RustFS 模型公共读

> 目标：让模型包可以被匿名下载，但**只开放模型前缀**，不影响 `storage1` 里的录音、备份等其他数据，也不重启 RustFS 或当前 lab 服务。

## 端口说明

| 端口 | 作用 |
|---|---|
| **9000** | S3 API（rclone / aws CLI / 匿名 GET） |
| **9001** | RustFS 控制台（浏览器登录查看） |

公共读策略作用在 **9000 的 S3 API**；9001 只是管理界面。

## 已配置的策略

对两个 bucket 生效：

- `english-lab`
- `storage1`

只允许：

- `s3:GetObject`：`<bucket>/rustfs/english-lab/models/*`
- `s3:ListBucket`：仅当 prefix 为该模型前缀

**不允许**写入、删除、列举其他前缀。`storage1/recordings/`、`db-backups/` 等保持私有。

## 公共 URL

从 Windows 浏览器：

```text
http://localhost:9000/english-lab/rustfs/english-lab/models/models.tar
http://localhost:9000/english-lab/rustfs/english-lab/models/models.tar.sha256
```

从 WSL：

```text
http://172.19.160.1:9000/english-lab/rustfs/english-lab/models/models.tar
```

`storage1` 把路径中的 `english-lab`（bucket）换成 `storage1` 即可。

## 验证结果

```text
english-lab:
  checksum GET    200
  range GET       206（1024 bytes）
  prefix list     200
  anonymous write 403

storage1:
  model GET       200
  recordings GET  403
  recordings list 403
  model list      200
  anonymous write 403
  anonymous delete 403

本地 lab_server /health: ok
```

## 修改/回滚

脚本：`scripts/rustfs-public-read.sh`

```bash
# 查看当前策略与匿名访问状态
RUSTFS_ENDPOINT=http://172.19.160.1:9000 \
RUSTFS_ACCESS_KEY=... RUSTFS_SECRET_KEY=... \
bash scripts/rustfs-public-read.sh status

# 应用（幂等；保留其他未管理的策略语句）
RUSTFS_ENDPOINT=http://172.19.160.1:9000 \
RUSTFS_ACCESS_KEY=... RUSTFS_SECRET_KEY=... \
bash scripts/rustfs-public-read.sh apply

# 回滚：只删除本脚本管理的两个 Sid；若没有其他语句则删除 bucket policy
RUSTFS_ENDPOINT=http://172.19.160.1:9000 \
RUSTFS_ACCESS_KEY=... RUSTFS_SECRET_KEY=... \
bash scripts/rustfs-public-read.sh remove
```

默认 bucket 列表是 `english-lab storage1`，可用 `RUSTFS_BUCKETS` 覆盖；前缀用 `RUSTFS_PUBLIC_PREFIX` 覆盖。

## 细粒度：单文件 / 单目录 / 读或写

S3/RustFS 没有 POSIX 文件权限，但 bucket policy 可以精确到 **单个对象 ARN** 或 **目录前缀**。

### 单个文件只读

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOneFile",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::english-lab/rustfs/english-lab/models/models.tar"]
    }
  ]
}
```

只允许这一个对象匿名下载；同目录其他文件仍然 403。

### 单个目录只读

```json
"Resource": ["arn:aws:s3:::english-lab/rustfs/english-lab/models/*"]
```

`/*` 表示该前缀下所有对象。需要匿名列目录时再加 `s3:ListBucket`，并用 `s3:prefix` 限制：

```json
{
  "Sid": "ListOneDir",
  "Effect": "Allow",
  "Principal": "*",
  "Action": ["s3:ListBucket"],
  "Resource": ["arn:aws:s3:::english-lab"],
  "Condition": {"StringLike": {"s3:prefix": ["rustfs/english-lab/models/*"]}}
}
```

### 单个目录可写

```json
"Action": ["s3:PutObject"]
```

把 `Resource` 设为目录前缀（如 `.../uploads/*`）即可让指定前缀可写。**不要把 `s3:PutObject` 配给 `Principal: "*"`**：那等于允许任何人上传/覆盖文件。写入应使用：

- 受控的 RustFS 用户/凭据；
- 或临时的 presigned URL（由服务端生成，限定 key 和有效期）；
- 或由你的后端代理上传。

### 实测对比（隔离测试桶，已删除）

| 配置 | 结果 |
|---|---|
| 精确到 `dir/readme.txt` 的匿名读 | `readme.txt` 200，`dir/secret.txt` 403 |
| 只允许 `dir/upload/*` 的匿名写 | 前缀内 PUT 200，前缀外 PUT 403 |
| 对象 ACL `public-read` | 匿名 GET 仍 403（该 RustFS 版本不以 ACL 放行匿名读） |
| presigned GET URL | 200 |

结论：**单文件/单目录的读或写都能做，最可靠的是 bucket policy；对象 ACL 不要依赖。**

### 使用限制

- Bucket policy 有大小上限（S3 兼容实现通常约 20 KB）；不要为成百上千个文件逐条写，优先用目录前缀或拆分 bucket。
- 策略是 bucket 级别的；要保留现有模型公共读，新增语句要合并到现有 `Statement` 数组里，不要直接覆盖。
- 公共写非常危险；如果只是临时上传，用 presigned URL 或后端代理更安全。

## 注意

- 修改 bucket policy 是 S3 控制面操作，**不需要重启 RustFS**，也不会影响当前运行的 `lab_server`。
- `AWS CLI` 已安装；脚本用环境变量传凭据，不写配置文件。
- 如果要完全恢复私有：运行 `remove`，再用匿名 GET 确认返回 403。
- 公共读只针对模型包；不要把整个 `storage1` 桶设为公共，里面包含录音和备份。
- 控制台 `9001` 直接 `curl` 返回 403 是正常的，需要登录。

## 相关

- [[deploy/README|Docker Swarm 部署]]
- [[deploy/upload-status|RustFS 权重上传记录]]
- [[scripts/upload-weights.sh|权重上传脚本]]
