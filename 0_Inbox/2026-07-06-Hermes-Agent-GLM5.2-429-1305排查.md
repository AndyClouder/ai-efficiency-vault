---
date: 2026-07-06
source: https://deeprouter.org/article/hermes-agent-optimization-fix-glm-5-2-model-429-1305-overloaded
short_link: https://share.google/fWQEXfaI8SopNJtgR
raw: 0_Inbox/raw/2026-07-06_Hermes-Agent-GLM5.2-429-1305_raw.md
author: Yawatasensei
site: Deep Router (deeprouter.org)
tags: [Hermes-Agent, GLM-5.2, 429排查, 客户端指纹, prompt-caching]
status: inbox
---

# Hermes Agent 优化：解决 GLM-5.2 模型 429(1305 overloaded)

## 核心要点

- **"假 429" 的判别**：同 key、同 endpoint、同 model、同请求长度，唯一变量是 system prompt 内容——含精确短语 `Hermes Agent` 时返回 429 / `code 1305`，改成 `Hermes framework` 立刻 200。这是 Z.AI Coding Plan 后端的内容过滤，不是限流。
- **不能全库 sed 替换**：`Hermes Agent` 一词在 `~/.hermes` 下 50+ 处(SOUL.md / skills / 内置常量 / 已持久化 session),一刀切会污染技能库、漂移历史 session、被官方更新覆盖静默复发。
- **解法：改请求路径不改磁盘**。在 `build_system_prompt()` 返回尾、且经 `provider=="zai" && "glm-5.2" in model` 双重 gate 后做原地替换;这是 session 初始化/context 重建的合法缓存边界,不破坏 prompt caching invariant。
- **第二层：客户端指纹 Headers**。Z.AI 网关会通过 `User-Agent`/`X-Stainless-*` 等 SDK 特征头识别非官方客户端并拒绝。Hermes 已有 per-provider header 注入机制(Kimi/Copilot/NVIDIA/Qwen),依葫芦画瓢加 Z.AI 分支注入 `User-Agent: ZCode/0.14.8` 等指纹头。
- **5 条经验**:① 不是所有 429 都是限流 ② 改请求路径不改数据 ③ Provider gate 是底线 ④ Prompt caching invariant 不能破 ⑤ 客户端指纹检测越来越常见。

## 原文摘要

作者把 Hermes Agent 主模型从 DeepSeek V4 Pro 切到 `zai/glm-5.2` 后,首请求直接吃 429/code 1305。初步排查排除:额度充足(5h/周额度 >90%)、换新 key 无效、降请求长度(砍 tools / 清 history / 缩 system prompt 到几百字)均无效。但同 key 用 curl 裸调短 prompt 能通。

关键转折是 GitHub issue `NousResearch/hermes-agent#47685`——复现极其干净:**唯一变量是 system prompt 是否包含精确短语 `Hermes Agent`**。结论:Z.AI Coding Plan 后端对 system prompt 做了内容检测(产品名/客户端指纹/或 WAF 误伤),披着 429 的皮。

### 真凶藏在哪

全局搜 `Hermes Agent` 命中 50+ 处:`SOUL.md`(身份定义)、`skills/**/SKILL.md`、`agent/system_prompt.py`(内置 guidance 常量)、`agent/prompt_builder.py`(DEFAULT_AGENT_IDENTITY)、`sessions/*.sqlite`(已持久化 system_prompt)。所以不是改一个配置文件能解决的。

### 为什么不全库 sed 替换

三个坑:① 污染技能库(精心调过的定义被破坏语义) ② 污染历史 session(resume 时语义漂移) ③ 被官方更新覆盖、改动静默丢失、bug 复发。

### 双层修复方案

**第一层 — System Prompt 内容替换**:在 `agent/system_prompt.py` 的 `build_system_prompt()` 返回尾加替换逻辑,gate 条件是 `provider == "zai"` + `"glm-5.2" in model_lower`。放这里是因为 Hermes 的 prompt caching 是 sacred——session 内部 turn 循环直接读 `_cached_system_prompt`,只有 session 初始化和 context 重建时才走 `build_system_prompt()`,都是合法缓存边界,替换不影响 session 内 cache 稳定性。

**第二层 — 客户端指纹 Headers**:Z.AI 网关通过 HTTP headers 判断请求来源。官方 ZCode 客户端带 `User-Agent: ZCode/0.14.8` / `X-ZCode-App-Version: 0.14.8` / `X-ZCode-Agent: glm`,而 Hermes 默认带的是 OpenAI Python SDK 的 `User-Agent: OpenAI/Python ...` + `X-Stainless-*`,被网关当作非官方客户端拒绝。Hermes 已有 per-provider header 注入机制(`_apply_client_headers_for_base_url`),为 Z.AI 加一个分支即可。注入点共 4 处:pool 解析、credential 解析、async 转换、custom endpoint resolution。

### 验证

重启 Hermes 切 `zai/glm-5.2`,发消息成功返回无 429。覆盖测试:Z.AI glm-5.2 替换生效 ✓ / 非 Z.AI provider 不替换 ✓ / Z.AI base_url 注入 ZCode headers ✓。

### 5 条经验总结

1. **不是所有 429 都是限流** —— 特定 provider + model + prompt 内容组合下,优先考虑内容过滤。curl 裸调能通而完整请求挂,"假 429"概率远高于真限流。
2. **改请求路径,不改数据** —— 磁盘上的 SOUL.md/skills/session 是资产,运行时请求是可变流量。全库 sed 会把修 bug 变成埋雷。
3. **Provider gate 是底线** —— 任何 provider-specific workaround 必须 gated(这次是 zai + glm-5.2),全局改动会制造幽灵 bug。
4. **Prompt caching invariant 不能破** —— system prompt 修改必须在构建边界做,不能在 turn 循环里做,否则每轮多烧一倍 token。
5. **客户端指纹检测越来越常见** —— 从 Kimi(要求 `User-Agent: claude-code/0.1.0`)到 Z.AI(要求 ZCode headers),遇到"同 payload 不同客户端行为不同"先查 HTTP headers。

## 来源

- 原文:https://deeprouter.org/article/hermes-agent-optimization-fix-glm-5-2-model-429-1305-overloaded
- 短链:https://share.google/fWQEXfaI8SopNJtgR
- 作者:Yawatasensei · Deep Router (deeprouter.org)
- 关键引用:GitHub Issue `NousResearch/hermes-agent#47685`
- 保存日期:2026-07-06
