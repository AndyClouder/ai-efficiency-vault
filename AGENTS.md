# AGENTS.md — ZCode 工作区指令

> 📌 **本文件是 `0_系统配置/CLAUDE.md` 的引用式派生（ZCode 版）。**
> 本文件**不复制** canonical 正文——所有 agent 通用规则（身份、语言、Skill 路由、记忆系统、知识管理铁律、安全规则等）一律以 canonical 为准。
> 本文件只写 **ZCode 工作区专属**的东西。改 agent 规则请改 canonical，本文件仅在 ZCode 有特殊约束时才动。

---

## agent 配置架构（canonical → 派生）

```
0_系统配置/CLAUDE.md  ← CANONICAL（唯一可编辑的 agent 配置真身）
        │
        ├─ 标题投影（Claude Code→Codex）→ 0_系统配置/AGENTS.md  ← 生成物·勿手改
        │
        └─ 引用式派生（手写精简）──────→ 根目录 AGENTS.md (ZCode，即本文件)
```

**派生分两类（加新 agent 时按此选）：**
- **近一致**（仅标题/声明不同）→ 走"标题投影"：从 canonical 复制 + 替换标题 + 改声明，归一化后逐字一致
- **刻意不同**（如 ZCode 的精简版）→ 走"引用式派生"：手写，指向 canonical，不复制正文

**派生一致性由「配置审查」检查 ⑤ 守护**（对投影做标题归一化后逐字比对）。

---

## ZCode 工作区专属规则

以下规则是 **ZCode 运行环境特有**的，canonical 里没写（因为 Claude Code / Codex 不需要）：

### Skill 四镜像同步（修改任何 Skill 时强制）

Skill 在四处目录镜像存放，**内容必须完全一致**：
- 配置源（同步基准，不被直接加载）：`0_系统配置/.agents/skills/`、`0_系统配置/.claude/skills/`
- 运行时副本（Agent 实际加载）：`.agents/skills/`、`.claude/skills/`

修改流程：改两个源 → `cp -r` 到两个运行时副本 → `md5sum` 校验四处 `SKILL.md` 一致。
当前对齐 10 个 skill：图绘大师、新手引导、恢复初始化、知识入库、知识分类、知识编译、知识问答、知识体检、网络调研、配置审查。

### 平台/路径注意

- Windows + Git Bash 环境；路径含中文与空格，shell 命令务必加引号。
- 相对路径从 vault 根出发，**不加前导 `/`，不用 `C:\` 绝对路径**。
- 图绘大师等导出到 vault 根 `ppt_outputs/`（已在 `.gitignore`）。

### ZCode 特有约定

- 涉及破坏性操作（删文件、覆盖、重置）时，先向用户确认再执行——ZCode 的权限模式由用户控制。
- 根目录的 `.zcode/` 目录（若存在）由 ZCode 客户端管理，不要手动改。

---

## 必读的 canonical 内容（涉及对应场景时回查）

| 用途 | 在 canonical 里的位置 |
|------|---------------------|
| 完整 Skill 路由表 + 触发词 | `0_系统配置/CLAUDE.md` 的「⚡ Skill 路由」节 |
| 强制启动协议（每次新对话先加载 SOUL/USER/MEMORY） | 「记忆系统」节 |
| 记忆写入规则（8 条 + 通知格式） | 「记忆写入规则」节 |
| INDEX/LOG 双铁律、原文保全铁律、复利原则 | 「索引与日志双铁律」「知识管理规则」节 |
| 安全与事实规则 | 「安全与事实规则」节 |

> 完整内容直接读 `0_系统配置/CLAUDE.md`。本文件不重复抄录。

---

*版本：v2.0 · 派生自 `0_系统配置/CLAUDE.md`（canonical）· 2026-07-06*
