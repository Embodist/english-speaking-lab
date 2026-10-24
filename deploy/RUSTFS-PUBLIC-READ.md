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
