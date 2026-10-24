---
type: record
title: RustFS 权重上传记录
tags: [deploy, meta]
created: 2026-10-24
updated: 2026-10-24
---

# RustFS 权重上传记录

## 位置 A：english-lab（推荐用于部署）

| 项目 | 值 |
|---|---|
| Endpoint | `http://172.19.160.1:9000`（WSL → Windows RustFS） |
| Bucket | `english-lab` |
| Prefix | `rustfs/english-lab/models/` |
| Object | `models.tar` |
| Size | `2,805,063,680` bytes（约 2.61 GiB） |
| SHA256 | `0b4d49c4b8360cfd18883f7b65a508d907cf2bdef56654eb66c3269a79b20a7d` |
| 校验 | `rclone check`：0 differences，2 matching files（2026-10-24 08:46） |

对象内容：OpenPronounce 两个 Wav2Vec2 检查点、Piper 声音、Whisper `base.en`、Vosk 小模型。容器入口会解压到 `/models`。

## 位置 B：storage1（你指定的桶，已验证）

| 项目 | 值 |
|---|---|
| Bucket | `storage1` |
| Prefix | `rustfs/english-lab/models/` |
| Object | `models.tar` |
| Size | `2,805,063,680` bytes（约 2.61 GiB） |
| SHA256 | `0b4d49c4b8360cfd18883f7b65a508d907cf2bdef56654eb66c3269a79b20a7d` |
| 校验 | `rclone check`：0 differences，2 matching files（2026-10-24 08:56） |

说明：

- `storage1` 第一次整包上传时返回 `503 ServiceUnavailable` / 扫描超时；`rustfs` 作为桶名被 RustFS 判为非法。
- 改用 `--s3-chunk-size 16M --s3-upload-concurrency 2` 重试后成功。
- 目前 `english-lab` 和 `storage1` 两处内容一致；默认部署建议用较干净的 `english-lab`，需要时可用 `RUSTFS_BUCKET=storage1`。

## 重新上传

```bash
cd ~/english/english-speaking-lab
source deploy/rustfs.env
export RUSTFS_ACCESS_KEY='...'
export RUSTFS_SECRET_KEY='...'
bash scripts/upload-weights.sh
```

`scripts/upload-weights.sh` 默认使用 `english-lab/rustfs/english-lab/models/`；要传 `storage1`：

```bash
RUSTFS_BUCKET=storage1 bash scripts/upload-weights.sh
```

## 注意

- 不记录 access/secret；上传使用环境变量，Docker 使用 secrets。
- RustFS 默认凭据较弱，部署前请修改。
- `models.tar.sha256` 里的文件名是相对路径 `models.tar`，容器里可直接 `sha256sum -c`。

## 相关

- [[deploy/README|Docker Swarm 部署]]
- [[scripts/upload-weights.sh|上传脚本]]
