---
type: topic
title: PR 与 Code Review
tags: [scene/pr, skill/speaking, status/learning]
created: 2026-10-23
updated: 2026-10-23
---

# PR 与 Code Review

## 高频句

- `I’ve opened a pull request for the change.` — 我为这个改动开了 PR。
- `Could you take a look when you have a chance?` — 有空能帮忙看一下吗？
- `The PR is ready for review.` — PR 已准备好审查。
- `I’ve addressed the comments.` — 已处理评论。
- `I pushed a follow-up commit.` — 又推了一个补充提交。
- `Could you clarify why this branch is needed?` — 能说明为什么需要这个分支吗？
- `This change looks good to me.` — 这个改动我觉得没问题。
- `I have one small suggestion.` — 有一个小建议。
- `Could we extract this into a helper function?` — 能否提取成辅助函数？
- `This logic is duplicated in two places.` — 这段逻辑在两个地方重复。
- `Could we add a test for the empty-input case?` — 能否增加空输入测试？
- `This is a nit, not a blocker.` — 小细节，不是阻塞项。
- `I’ll merge it once CI passes.` — CI 通过后合并。
- `Let’s keep this PR focused on one concern.` — PR 尽量只关注一个问题。
- `The change is backward-compatible.` — 改动向后兼容。
- `I’ll rebase on the latest main branch.` — 基于最新 main rebase。

## 礼貌评论模板

| 目的 | 句型 |
|---|---|
| 建议 | `Could we …? It would make … easier to …` |
| 疑问 | `Could you help me understand why …?` |
| 潜在问题 | `I’m concerned this may fail when …` |
| 阻塞 | `I think we should address this before merging because …` |
| 可选 | `Non-blocking suggestion: …` |

## 示例

> Could we extract the retry logic into a helper function? It would make the error handling easier to test. Non-blocking suggestion—the current version works, but the duplication may drift over time.

## 练习

- [ ] 给最近一个 PR 写 3 条评论：1 建议、1 疑问、1 非阻塞
- [ ] 录制 30 秒 PR 说明：改了什么、为什么、测试覆盖

## 相关

- [[02_daily-work/_index|日常工作]]
- [[08_sentence-library/daily-work|日常工作句子库]]
