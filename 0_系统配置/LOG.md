---
description: 知识库时间线日志。只追加不修改，每条统一前缀，可用 grep 快速查看近况。
updated: 2026-08-14
---

# LOG — 知识库时间线

> 格式：`## [YYYY-MM-DD] 操作类型 | 摘要`
> 操作类型：ingest（入库）/ classify（分类）/ compile（编译）/ query（问答）/ research（调研）/ lint（体检）/ reset（重置）/ system（系统变更）
> 快速查看最近 5 条：`grep "^## \[" 0_系统配置/LOG.md | tail -5`

---

## [2026-07-07] reset | 知识库恢复初始化

## [2026-07-13] ingest | 法本需求调研Skill操作手册

## [2026-07-13] classify | 共1篇：移动1，跳过0（→ 3_Resources/操作手册/）

## [2026-08-03] ingest | 高力集团AI智能化需求（售前）建档入 1_Projects/，四大方向需求存档，材料待启动

## [2026-08-03] ingest | 高力国际客户需求说明原文保全入库；主档更新：客户定位修正为 Colliers（商业地产五大行），新增客户主体识别+决策链分析，补完整闭环目标

## [2026-08-03] system | 项目重命名 高力集团→高力国际（目录+主档文件名+INDEX 链接+Wiki Link 同步）

## [2026-08-03] compile | 高力国际售前 PPT v1.0 生成（ppt-master，23 页，套 FarAI 风格，pyramid+soft-rounded，0 error 通过质检，含 23 页演讲者备注）

## [2026-08-05] system | 新增 2 个 skill：farai-style-conversion（FarAI 品牌风格转化器）+ presales-ppt-authoring（售前 PPT 编写）；各含 references 子目录；四镜像 MD5 全部一致；CLAUDE.md 路由表已更新

## [2026-08-05] ingest | AI研发流水线售前材料建档：两份外部思想材料（吴穹5+2万字长文 + Kanban2 Agent Harness v22 PDF）原文保全入库到 1_Projects/AI研发流水线/需求原文/，建项目主档，口径定为完全自包装为法本 FarAI 体系

## [2026-08-05] compile | FarAI 研发流水线售前 PPT v1.0 生成（presales-ppt-authoring → farai-style-conversion → ppt-master 全流程）：27 页标准售前范式（A 行业趋势补强 P22 + B 反模式对比 P21），套 FarAI 风格（深蓝/微软雅黑/soft-rounded/pyramid），svg_quality_checker 27/27 通过（0 error/0 warning/spec_lock 零漂移），78 图标嵌入 + 201 圆角矩形转 path + 27 页演讲者备注，导出 PPTX 到 projects/FarAI研发流水线_ppt169_20260805/exports/

## [2026-08-05] compile | FarAI 研发流水线售前 PPT v1.1 修订：用户反馈 5+2 新范式（新组织/FDE 团队）未涉及，新增第三章「组织重塑」4 页（P10 章节封面 + P11 新角色 Builder + P12 新组织 FDE 三层协同 + P13 新流程三层流动），原 27 页重排为 30 页 6 章结构，5+2 七维度全覆盖；svg_quality_checker 31/31 通过，重新导出 PPTX 到 exports/FarAI研发流水线_20260805_172347.pptx

## [2026-08-12] ingest | 专业内容转外行指南（Skill）入库：两阶段流程（分析→写作）把专业资料转外行能懂的文档，含六层概念讲解+四层例子展开+认知Gap四类搭桥；原文存证于 0_Inbox/raw/

## [2026-08-12] classify | 共1篇：移动1，跳过0（→ 3_Resources/操作手册/）

## [2026-08-12] compile | 专业内容转外行指南 → 触及 1 页（新建 1：[[FDE]] 概念页；修订 0；矛盾 0、张力 1 记为待裁决）；新增笔记间关联 2 对（本笔记↔法本需求调研操作手册 双向，双方均链入 FDE 页）

## [2026-08-14] compile | FDE 经分会材料增补：新素材《企业FDE人才：招聘还是内部培养》四阶段框架融入——大纲重写 P16（先想能力不想岗位+双视角：客户阶段1–2=法本市场窗口/法本自身人才策略）、新增 P17（4特质选人+项目制培养），20→21 页；映射文档补 4 处（④⑤段素材表+对齐表第8条背书链+速查表）；补登记 FDE材料准备 项目进 INDEX（8-12 建档时漏登）

## [2026-08-14] compile | FDE 经委会汇报 PPT v1.1 增量修订：四阶段人才框架页落进 PPT——新增 21_人才策略四阶段.svg（四阶段 chevron+四卡+双视角带）、原 21 人才页改写为 22_内部挖人（4特质卡+项目制培养），21–25 顺延为 22–26，25→26 页；spec_lock/design_spec/notes/total.md 同步；svg_quality_checker 26/26 通过（0 error/0 warning/0 漂移），重新导出 exports/FDE经委会汇报_20260814_164017.pptx

## [2026-08-18] lint | 全库体检（reset 后首次重算）：知识笔记 20 篇 / 综合页 1 / 问题 🔴5 🟡3 🟢23（死链 5 多为 reset 遗留；重复 2 对；陈旧结论 1 页/待编译 2；孤立 13；无fm 7；缺口 3）/ 已修复：无（待指令）；DASHBOARD 已重算，报告归档 体检报告/2026-08-18.md

## [2026-08-18] system | 知识生命周期升级（借鉴《LLM Wiki v2》）：①置信度尾标 ②墓碑替代链 ③衰减候选 ④方法页（程序性记忆）⑤类型化关系 ⑥项目结项结晶；改知识编译/知识问答/知识体检 3 skill 四镜像 MD5 一致；canonical 更新 + AGENTS.md 投影重生成（顺带修复投影缺 2 行路由的旧漂移）；5_Wiki 说明+方法页目录+项目模板+INDEX 同步

## [2026-08-18] compile | 示范编译（新机制首跑）：《企业FDE人才：招聘还是内部培养》+《FDE到底该招还是自己培养》→ 触及 1 页（修订 1）：[[FDE]] 新增「人才策略四阶段」侧面（本页首个 2 源加固条目），矛盾补"能力先行"新证据仍未澄清；铺类型化关联 2 对；顺带修复 3 个 reset 死链（移除 07-02 编译器越权写入 raw 的"相关"节恢复原文）+ 1 个 skill 伪链接（farai-style-conversion）

## [2026-08-19] system | 新增 0_系统配置/PURPOSE.md（库罗盘，借鉴 llm_wiki 的 purpose 设计，与 schema 分离）：目标三层（资产/方法论/示范）+ 4 关键问题（FDE 落地/售前流水线/需求调研规模化/系统复利）+ 范围 + 主论点（FDE 组织承接论，库内证据支撑，待用户裁决）+ 当前焦点 4 项；纳入强制启动协议四件套（SOUL/USER/MEMORY/PURPOSE）；canonical + Codex 投影（0_系统配置/AGENTS.md）+ ZCode 派生（根 AGENTS.md）三处同步。INDEX 未动（系统文件不入内容目录，循 8-18 先例）

## [2026-08-19] system | 仓库内容策略变更：.gitignore 排除二进制内容资产（*.pdf/*.pptx/*.png/*.gif/*.jpg/*.jpeg），49 个已跟踪二进制（约 92M，公众号配图/PPTX 交付物/PDF 资料）移出版本控制——本地文件保留不动，仅远程不再存储；skills 的 py/svg 功能文件不受影响（目录内无二进制）。原因：92M 二进制导致推送反复超时，远程定位为 md 知识库
