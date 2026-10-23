---
type: hub
title: 录音与附件
tags: [hub, skill/pronunciation]
created: 2026-10-23
updated: 2026-10-23
---

# 录音与附件

所有音频、截图放这里。Obsidian 的附件目录已指向本文件夹。

## 命名规范

```text
day<NN>_<scene>_<take>.wav
day01_intro_baseline.wav
day01_intro_first-take.wav
day01_intro_corrected.wav
day09_standup_first-take.wav
```

## 录音来源

### 方式 A：手机录音（最简单）
1. 手机录音 App 录 30–60 秒。
2. 传到电脑，复制到本文件夹。
3. 用 `ffmpeg` 转成 WAV（OpenPronounce 兼容性最好）：

```bash
ffmpeg -i input.m4a -ar 16000 -ac 1 output.wav
```

### 方式 B：Windows 录音机
1. Windows 搜索「录音机 / Voice Recorder」。
2. 录音后文件默认在 `C:\Users\<你>\Documents\Recording`。
3. 在 WSL 中复制：

```bash
cp "/mnt/c/Users/<你>/Documents/Recording/*.m4a" ~/english/english-speaking-lab/11_attachments/
```

### 方式 C：OpenPronounce 网页界面
浏览器打开 `http://localhost:8000`，直接录音并分析。浏览器麦克风需要 `localhost` 或 HTTPS。

## 检查清单

- [ ] 安静环境、固定麦克风距离
- [ ] 一次连续录完，不逐词暂停
- [ ] 文件名符合规范
- [ ] 保留第一次录音，不要覆盖

## 相关

- [[01_pronunciation/_index|发音训练]]
- [[09_sources/英语口语训练手册_程序员面试与职场沟通#2. 每日训练流程：20–30 分钟的固定闭环|每日流程]]
