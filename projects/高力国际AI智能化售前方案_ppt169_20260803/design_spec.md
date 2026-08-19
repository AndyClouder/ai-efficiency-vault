# 高力国际AI智能化售前方案 - Design Spec

> 人类可读的设计叙述——背景、受众、风格、配色、内容大纲。由下游角色一次性阅读获取上下文。
> 机器可读的执行契约见 `spec_lock.md`。两者保持同步;冲突时以 `spec_lock.md` 为准。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 高力国际 AI 智能化售前方案 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 23 |
| **Design Style** | FarAI 企业科技风(深蓝主色 + 圆角卡片网格 + 金字塔结论先行) |
| **Target Audience** | 客户决策层(高力国际高管/业务负责人) |
| **Use Case** | 售前方案汇报,支撑商务推进 |
| **Created Date** | 2026-08-03 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px,上下 50px |
| **Content Area** | 1160×620(标题区 1160×80,正文区 1160×500,页脚区 1160×40) |

---

## III. Visual Theme

### Theme Style

- **Mode**: `pyramid` — 结论先行,MECE 论证,每个数据带对比。售前决策支持场景的标准骨架:先抛价值主张,再展开方案,最后落到价值闭环与实施。
- **Visual style**: `soft-rounded` — 圆角卡片、温和立体感、企业产品风。与 FarAI 参考材料的白底深蓝圆角卡片网格一致。
- **Theme**: Light theme(白底,与 FarAI 参考一致)
- **Tone**: 专业、稳重、科技感、可信赖。商业地产 + AI 双重属性:地产要稳重,AI 要创新。

### Color Scheme

> 用户明确要求套用 FarAI 品牌色——以下 HEX 直接锁定,跳过推荐表。

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 页面背景(白底) |
| **Secondary bg** | `#F4F7FC` | 卡片背景/分区背景(极浅蓝灰) |
| **Primary** | `#0052A6` | 品牌主色:标题装饰、关键区块、图标主色(FarAI 深蓝) |
| **Accent** | `#246BFE` | 数据高亮、关键信息、强调亮蓝 |
| **Secondary accent** | `#518FEC` | 次级强调、渐变过渡 |
| **Body text** | `#25364A` | 正文(深) |
| **Secondary text** | `#5E6A78` | 正文(灰)、注释 |
| **Tertiary text** | `#6B7785` | 辅助信息、页脚 |
| **Border/divider** | `#E3E9F2` | 卡片边框、分隔线(浅蓝灰) |
| **Success** | `#0E9F6E` | 正向指标(绿) |
| **Warning** | `#F59E0B` | 提醒/中等(橙) |
| **Info** | `#20A7B8` | 辅助分类(青) |

### Gradient Scheme

```xml
<!-- 章节封面/封面标题渐变 -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#0052A6"/>
  <stop offset="100%" stop-color="#246BFE"/>
</linearGradient>

<!-- 章节封面背景渐变(深蓝) -->
<linearGradient id="chapterBg" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#0A2A5E"/>
  <stop offset="100%" stop-color="#17365D"/>
</linearGradient>

<!-- 背景装饰渐变 -->
<radialGradient id="bgDecor" cx="85%" cy="15%" r="50%">
  <stop offset="0%" stop-color="#246BFE" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#246BFE" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: 现代 CJK 无衬线,与 FarAI 参考一致(微软雅黑)。标题加粗显权重,正文常规保可读。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `"Microsoft YaHei", Arial, sans-serif`(Bold)
- Body: `"Microsoft YaHei", Arial, sans-serif`(Regular)
- Emphasis: `"Microsoft YaHei", Arial, sans-serif`(SemiBold/Bold)
- Code: `Consolas, "Courier New", monospace`

> Concord 同族方案:全篇微软雅黑,靠字重(Bold/Regular)与字号拉开层级。与 FarAI 参考完全一致,PPT-safe,跨平台稳定。

### Font Size Hierarchy

**Baseline**: Body font size = **18px**(信息密度较高的售前方案)

| Purpose | Ratio | px @ body=18 | Weight |
| ------- | ----- | ------------ | ------ |
| Cover title(封面主标题) | 2.5-5x | 56px | Bold |
| Chapter opener(章节封面) | 2-2.5x | 40px | Bold |
| Page title(页面标题) | 1.5-2x | 30px | Bold |
| Hero number(关键数据) | 1.5-2x | 32px | Bold |
| Subtitle(副标题) | 1.2-1.5x | 24px | SemiBold |
| **Body content(正文)** | **1x** | **18px** | Regular |
| Annotation(注释) | 0.7-0.85x | 14px | Regular |
| Page number(页脚) | 0.5-0.65x | 11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 顶部 50-130px。左上角章节小标签(14px 灰)+ 页面主标题(30px 深蓝粗体)+ 可选副标题(18px 灰)
- **Content area**: 中部 460-520px。卡片网格 / 流程横排 / 矩阵,随页面内容而定
- **Footer area**: 底部 30-40px。右下角页码(11px 浅灰),左下角"©法本信息"标识

### Layout Pattern Library

| Pattern | 适用于本方案的页面 |
| ------- | ----------------- |
| **Single column centered(单列居中)** | 封面、封底、章节封面 |
| **Four-quadrant / 2×2 matrix(四象限)** | P5 四大痛点、P20 价值矩阵 |
| **Three/four column cards(三/四列卡片)** | P4 客户认知、P9 产品矩阵、P22 保障 |
| **Top-bottom split(上下分区)** | P6 闭环流程、P8 架构图、P11-18 各场景流程 |
| **Center-radiating(中心辐射)** | P16 客户归并决策链 |
| **Z-pattern(瀑布)** | P21 实施路径阶段 |
| **Asymmetric split(3:7 / 2:8)** | P8 架构图(底座+场景层) |

### Spacing Specification

**Universal**:

| Element | Range | Current |
| ------- | ----- | ------- |
| 画布安全边距 | 40-60px | 60px |
| 内容块间距 | 24-40px | 32px |
| 图标-文字间距 | 8-16px | 12px |

**Card-based layouts**:

| Element | Range | Current |
| ------- | ----- | ------- |
| 卡片间距 | 20-32px | 24px |
| 卡片内边距 | 20-32px | 24px |
| 卡片圆角 | 8-16px | 12px |
| 双行卡片高度 | 265-295px | 280px |
| 三列卡片宽度 | 360-380px | 360px |

---

## VI. Icon Usage Specification

### Source

- **Icon library**: `tabler-outline`(线框、专业、企业感)
- **Stroke width**: 2(全局统一)
- **Usage**: SVG placeholder `<use data-icon="tabler-outline/<name>" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 商业地产/楼宇 | `tabler-outline/building` | P4,P8,P13,P16 |
| 招聘/人才 | `tabler-outline/users` | P11,P12 |
| 搜索/商机发现 | `tabler-outline/search` | P13,P14 |
| 投标/文件 | `tabler-outline/file-text` | P15 |
| 数据/分析 | `tabler-outline/chart-bar` | P17,P18,P20 |
| 目标/价值 | `tabler-outline/target` | P6,P20 |
| 闭环/复盘 | `tabler-outline/refresh` | P6,P21 |
| 安全/保障 | `tabler-outline/shield` | P22 |
| 完成核对 | `tabler-outline/circle-check` | P11,P14,P20 |
| 流程箭头 | `tabler-outline/arrow-right` | P6,P11,P13 |
| 智能/AI大脑 | `tabler-outline/brain` | P8,P9 |
| 录音/营销 | `tabler-outline/headset` | P17,P18 |
| 决策/网络 | `tabler-outline/network` | P16 |
| 灯泡/洞察 | `tabler-outline/bulb` | P14,P18 |
| 电话 | `tabler-outline/phone` | P18 |
| 机器人 | `tabler-outline/robot` | P12 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim from charts_index.json) | Usage |
| ---- | -------- | ---- | ------------------------------------------------- | ----- |
| P06 | process_flow | `templates/charts/process_flow.svg` | "Pick for a linear sequence of stages with a clear start and end (process, pipeline, customer journey). Skip if the stages loop back or run in parallel." | 业务闭环:信息发现→商机识别→客户归并→决策链→销售→投标→复盘 |
| P11 | process_flow | `templates/charts/process_flow.svg` | "Pick for a linear sequence of stages with a clear start and end (process, pipeline, customer journey). Skip if the stages loop back or run in parallel." | 招聘全流程:发布→收集→筛选→邀约→面试→跟踪 |
| P16 | hub_inward_arrows | `templates/charts/hub_inward_arrows.svg` | "Pick for one central entity fed by several surrounding contributors (ecosystem, stakeholder map, core-satellite). Skip if the contributors act on each other (use network_diagram)." | 决策链:核心客户+决策人/需求人/采购/评估/业主投资方等角色辐射 |

**Runners-up considered**:

- `numbered_steps` | rejected for P06: 闭环是横向首尾相连的业务流(非编号步骤列表),process_flow 的箭头串联更贴合"信息发现→...→复盘"的流向语义
- `network_diagram` | rejected for P16: 决策链是"核心客户 + 多角色向心"结构,各角色服务于同一客户而非相互交互,hub_inward_arrows 的中心辐射更准确;network_diagram 适用角色间多向互动场景
- `chevron_chain_with_tail` | rejected for P11: 招聘流程虽是链式,但每步需承载功能说明文字(发布/筛选/邀约),chevron 箭头形变窄不利于文字承载,process_flow 的等宽节点更合适

---

## VIII. Image Resource List

无图片(选项 A)。本方案纯图标 + 卡片 + 流程图,与 FarAI 智能投标参考 PPT 一致——决策层方案重价值逻辑不重配图,无图能让内容 100% 聚焦。所有视觉元素由 SVG 原生绘制 + tabler-outline 图标承载。

> 本方案无 image-as-canvas(#38-#46)页面的需求,因不使用任何位图。

---

## IX. Content Outline

### Part 1: 开篇(封面 + 目录)

#### Slide 01 - 封面

- **Layout**: Single column centered + 左侧色块装饰
- **Title**: `FarAI × 高力国际`
- **Subtitle**: 商业地产 AI 智能化解决方案
- **Info**: 深圳市法本信息技术股份有限公司 · 领先的软硬一体化、解决方案服务商 · 2026.08

#### Slide 02 - 目录

- **Layout**: Four column cards(四列卡片)
- **Title**: 目录 CONTENTS
- **Core message**: 四大章节构成完整方案叙事:客户理解 → 总体方案 → 场景方案 → 价值实施
- **Content**:
  - 01 客户理解与价值主张 / Customer Insight
  - 02 总体方案架构 / Overall Solution
  - 03 四大场景方案 / Scenario Solutions
  - 04 价值、实施与保障 / Value & Delivery

### Part 2: 第一章 客户理解与价值主张

#### Slide 03 - 章节封面 01

- **Layout**: Full-bleed 深蓝渐变 + 大章节号
- **Title**: 01 客户理解
- **Subtitle**: 与高力国际共建商业地产 AI 新基建

#### Slide 04 - 客户认知与价值主张

- **Layout**: Asymmetric split — 左侧客户认知(三列卡片),右下价值主张横幅
- **Title**: 高力国际 — 全球商业地产"五大行"之一
- **Core message**: 高力国际是商业地产全生命周期服务商,法本 FarAI 愿为其打造覆盖招聘—商机—投标—营销的 AI 闭环。
- **Content**:
  - 定位:全球商业地产"五大行"之一,非传统物业公司
  - 全生命周期服务:咨询策划 · 招商租赁 · 买卖交易 · 资产评估 · 工程管理 · 物业及资产管理
  - 服务对象:地产开发商 · 楼宇园区业主 · 投资机构 · 政府 · 大型企业
  - 业务特点:管理项目多 · 信息分散 · 销售跟进周期长 · 决策链复杂 · 一线招聘需求大
  - 价值主张:FarAI 以"一个平台 + 四大场景 + 一个闭环",让 AI 成为高力国际的增长新引擎

#### Slide 05 - 四大业务痛点

- **Layout**: Matrix grid 2×2(四象限卡片,每象限图标+痛点)
- **Title**: 四大业务痛点 — 高力国际的 AI 切入点
- **Core message**: 招聘、商机、客户、营销四个环节存在明确的人工瓶颈,正是 AI 的高价值切入点。
- **Content**:
  - 招聘量大流高:保安保洁基层岗位量大、流动性高,58同城等平台重复发布筛选邀约
  - 商机分散易漏:政府/招投标/短视频/招聘多渠道分散,人工收集效率低易遗漏
  - 客户分散难归并:同一楼宇/园区被多销售分散跟进,难识别同一客户、难还原决策链
  - 录音难回听:销售录音数量大依赖人工回听,话术规范/意向/商机难快速判断

#### Slide 06 - 整体价值闭环

- **Layout**: Top-bottom split — 上方横向流程图,下方价值说明
- **Title**: 整体价值闭环 — 从信息发现到结果复盘
- **Core message**: 四大场景串联成"信息发现→商机识别→客户归并→决策链分析→销售跟进→投标支持→结果复盘"的完整业务闭环(客户原话)。
- **Visualization**: process_flow(见 §VII)
- **Content**:
  - 七环闭环:信息发现 → 商机识别 → 客户归并 → 决策链分析 → 销售跟进 → 投标支持 → 结果复盘
  - 价值内核:多平台数据接入 · 音视频解析 · 客户主体识别 · 重复合并 · 决策链分析 · 商机评分 · 录音分析 · CRM/招聘/投标系统集成

### Part 3: 第二章 总体方案架构

#### Slide 07 - 章节封面 02

- **Layout**: Full-bleed 深蓝渐变 + 大章节号
- **Title**: 02 总体方案
- **Subtitle**: 一个平台、四大场景、一个闭环

#### Slide 08 - 总体架构图

- **Layout**: Top-bottom split — 三层架构(底座 / 场景层 / 集成层)
- **Title**: 总体架构 — FarAI 底座 × 四大场景 × 系统集成
- **Core message**: 以 FarAgent 平台为统一底座,向上承载四大场景应用,向下集成客户现有系统,形成端到端能力。
- **Content**:
  - 集成层(上):CRM 系统 · 招聘系统 · 投标系统 · 企业微信/OA
  - 场景层(中):智能招聘 · 智能商机 · 智能投标+客户归并 · 智能营销录音分析
  - 底座(下):FarAgent 平台(任务调度/分层记忆/进化引擎)+ 大模型 + 企业知识库 + 数据接入
  - 两侧:安全合规(私有化/权限/审计) · 生态合作(信通院/智谱/华为/哈工大)

#### Slide 09 - 产品矩阵映射

- **Layout**: Four column cards — FarAI 1+4+X → 高力四大场景
- **Title**: FarAI 1+4+X 产品矩阵 → 高力国际四大场景
- **Core message**: 法本 FarAI 现成的四大产品能力直接映射高力四大需求,无需从零建设。
- **Content**:
  - GPTRecruit → 智能招聘(JD生成/简历匹配/AI面试/招聘机器人)
  - FarAI 商机引擎(新建)→ 智能信息收集与商机识别(多源采集/解析/评分/分配)
  - GPTBidder + 客户归并(增强)→ 智能投标及客户关系分析(标书全流程+主体识别+决策链)
  - FarAI 录音分析(新建)→ 智能营销与销售录音分析(转写/多维分析/话术沉淀)
  - 底座 FarAgent:自主规划/沙盒执行/分层记忆/权限管理

### Part 4: 第三章 四大场景方案

#### Slide 10 - 章节封面 03

- **Layout**: Full-bleed 深蓝渐变 + 大章节号
- **Title**: 03 场景方案
- **Subtitle**: 四大场景逐一拆解痛点、流程与价值

#### Slide 11 - 智能招聘:痛点与全流程

- **Layout**: Top-bottom split — 上方痛点(横向4卡片),下方全流程
- **Title**: 智能招聘 — 基层岗位全流程自动化
- **Core message**: 从岗位发布到招聘过程跟踪,AI 覆盖基层招聘全链路,解放招聘人员的重复操作。
- **Visualization**: process_flow(见 §VII)
- **Content**:
  - 痛点:量大流频繁 · 简历质量参差 · 多平台重复 · 失联爽约到岗低 · 历史数据未沉淀
  - 全流程:岗位批量发布 → 候选人信息收集 → 基础条件筛选 → 自动沟通邀约 → 面试安排 → 招聘过程跟踪
  - 对象:保安/保洁/物业服务岗位;渠道:58同城等

#### Slide 12 - 智能招聘:核心能力与价值

- **Layout**: Three column cards(核心能力)+ 底部价值条
- **Title**: 智能招聘 — 核心能力与价值
- **Core message**: 五大核心能力让基层招聘效率与到岗率双提升,同时沉淀企业人才资产。
- **Content**:
  - 能力1 JD智能生成:解析岗位需求,自动生成高质量职位描述
  - 能力2 简历精准匹配:语义级"岗→人/人→岗"映射,初筛效率大幅提升
  - 能力3 AI面试:数字人模拟真实面试,千人千面出题,自动生成评估报告
  - 能力4 招聘机器人:自动登录平台筛选候选人并打招呼沟通,简历自动解析入库
  - 能力5 人才库沉淀:多渠道简历统一存储,历史候选人智能复荐
  - 价值(预估):简历筛选效率 ↑50%+ · 招聘周期 ↓40% · 简历采购成本 ↓30%

#### Slide 13 - 智能商机:痛点与多源采集

- **Layout**: Top-bottom split — 上方痛点(横向4卡片),下方6类商机+多源
- **Title**: 智能信息收集与商机识别 — 多源全量采集
- **Core message**: 从六大公开渠道持续采集商业地产商机,人工不再遗漏重要项目。
- **Content**:
  - 痛点:来源多而散 · 视频图片长文本提取难 · 重复缺去重 · 缺价值判断 · 难快速分配
  - 6类商机:新建写字楼/综合体/园区 · 城市更新及基建 · 楼宇出售/大宗交易/产权转让 · 楼宇易主/资产收购/股权变更 · 新项目招商及物业运营招标 · 企业搬迁扩建新办公场所
  - 多源采集:政府网站 · 公共资源交易平台 · 招投标平台 · 抖音等短视频 · 招聘平台 · 其他公开渠道

#### Slide 14 - 智能商机:智能解析与价值

- **Layout**: Asymmetric split — 左侧解析流程(纵向5步),右侧价值条
- **Title**: 智能信息收集与商机识别 — 解析·评分·分配
- **Core message**: 非结构化内容自动解析为结构化商机线索,按价值评分后秒级分配对应商务。
- **Content**:
  - 解析能力:网页/文档/图片/音视频非结构化内容采集解析
  - 提取字段:项目名称 · 项目地址 · 建筑面积 · 建设进度 · 业主单位 · 投资方 · 交易方 · 联系人 · 预算 · 招标时间
  - 价值判断:按客户规则判商机价值 → 优先级排序
  - 自动分配:结构化线索自动推送对应商务 → 记录来源/跟进/转化
  - 价值(预估):商机发现时效 天级→小时级 · 商机覆盖率 ↑3倍 · 重复信息自动去重

#### Slide 15 - 智能投标:投标流水线

- **Layout**: Top-bottom split — 上方6步投标流水线,下方说明
- **Title**: 智能投标 — 标书生产全流程智能化
- **Core message**: 从招标文件解析到投标材料完整性校验,AI 全流程辅助,降废标风险、提标书质量。
- **Content**:
  - 流水线:招标文件解析 → 资格条件识别 → 评分项拆解 → 历史材料匹配 → 标书内容辅助生成 → 风险检查 + 完整性校验
  - 痛点对照:文件多人工拆解易漏 · 历史标书难复用 · 评分点覆盖不充分 · 资格/废标/格式低级失误

#### Slide 16 - 客户归并与决策链 ⭐(重头)

- **Layout**: Center-radiating — 中心客户节点 + 多角色辐射(决策链)
- **Title**: 客户归并与决策链分析 — 统一客户视图(商业地产特色)
- **Core message**: 同一楼宇/园区被多销售分散跟进时,AI 自动归并为统一客户,并梳理完整决策链——这是高力国际的核心差异化价值。
- **Visualization**: hub_inward_arrows(见 §VII)
- **Content**:
  - 主体识别:结合企业名/项目名/楼宇地址/联系人/沟通记录/股权关系 → 判断是否同一客户/项目 → 统一客户视图
  - 决策链角色:最终决策人 · 业务需求提出人 · 采购招标负责人 · 项目使用部门 · 技术方案评估人 · 业主方/投资方/运营方/物业方
  - 关系洞察:各联系人关系与影响力 · 不同销售掌握信息与跟进情况
  - 痛点对照:同一客户重复跟进 · 名称不统一 · 信息分散在个人记录与录音 · 关键人物识别不清

#### Slide 17 - 智能营销:痛点与转写

- **Layout**: Top-bottom split — 上方痛点(横向5卡片),下方转写流程
- **Title**: 智能营销与销售录音分析 — 从录音到洞察
- **Core message**: 销售录音自动转写并多维分析,把停留在录音里的信息变成可行动的客户洞察。
- **Content**:
  - 痛点:录音量大无法逐条回听 · 缺统一沟通质量标准 · 真实需求商机易被忽略 · 优秀经验难沉淀 · 录音/客户/项目/任务未关联
  - 转写流程:销售电话/会议录音 → 语音转文字 → 按规则智能分析筛选

#### Slide 18 - 智能营销:多维分析与联动

- **Layout**: Four column cards(10大分析维度分四组)+ 底部联动条
- **Title**: 智能营销 — 十维分析 + 话术沉淀 + 客户联动
- **Core message**: 十个维度深度分析录音,优秀话术自动沉淀,分析结果回灌客户档案与决策链。
- **Content**:
  - 需求洞察:客户需求关注点提取 · 楼宇出售/易主/招商/物业更换商机识别
  - 意向判断:客户意向强弱判断 · 预算/时间/竞争对手/决策人信息提取
  - 质量评估:销售话术使用分析 · 关键问题是否问全 · 沟通质量评分
  - 合规与沉淀:风险词/承诺性/不规范话术识别 · 优秀话术沉淀与案例推荐 · 自动生成纪要与跟进建议
  - 联动:录音信息自动关联客户/项目/联系人/销售 → 补入客户档案与决策链

### Part 5: 第四章 价值、实施与保障

#### Slide 19 - 章节封面 04

- **Layout**: Full-bleed 深蓝渐变 + 大章节号
- **Title**: 04 价值与实施
- **Subtitle**: 商业价值、落地路径与法本保障

#### Slide 20 - 商业价值矩阵

- **Layout**: Matrix grid 2×2(四象限,每象限场景+量化指标卡片)
- **Title**: 商业价值矩阵 — 四大场景的效率·成本·收入提升
- **Core message**: 四大场景均带来可量化的效率提升、成本下降或收入增长机会(指标为预估值,可按实际校准)。
- **Content**:
  - 智能招聘:简历筛选效率 ↑50%+(预估) · 招聘周期 ↓40%(预估) · 简历采购成本 ↓30%(预估)
  - 智能商机:商机发现时效 天级→小时级(预估) · 商机覆盖率 ↑3倍(预估) · 重复信息自动去重
  - 智能投标:标书生产效率 ↑5倍(预估) · 废标风险 ↓50%(预估) · 历史标书资产可复用
  - 智能营销:录音分析覆盖率 100%(预估) · 商机识别响应 <1小时(预估) · 优秀话术可复制

#### Slide 21 - 实施路径

- **Layout**: Z-pattern / 三阶段瀑布
- **Title**: 实施路径 — 试点 · 扩展 · 闭环(3-6-12 月)
- **Core message**: 分三阶段稳步推进,先单场景试点验证价值,再横向扩展四场景,最后打通闭环持续运营。
- **Content**:
  - 阶段一 试点(0-3月):选 1-2 个高价值场景(建议智能招聘 + 智能商机)试点,验证价值,打通集成
  - 阶段二 扩展(3-6月):四大场景全面铺开,客户归并+决策链作为核心能力建设
  - 阶段三 闭环(6-12月):打通端到端闭环,沉淀企业知识资产,持续优化运营

#### Slide 22 - 法本保障

- **Layout**: Four column cards
- **Title**: 为什么是法本 — FarAI 能力底座 · 行业交付 · 安全合规 · 生态合作
- **Core message**: 法本以企业级 Agent 平台、大型客户交付经验、私有化安全能力和强生态合作,保障方案落地。
- **Content**:
  - FarAI 能力底座:FarAgent 平台 + 1+4+X 产品矩阵 + 大模型 + 知识库
  - 行业交付经验:大型客户项目管理 · 行业解决方案沉淀 · 企业系统集成
  - 安全合规:支持私有化/混合部署 · 权限控制 · 审计可追溯 · 数据安全
  - 生态合作:信通院 · 智谱 · MiniMax · 华为 · 哈工大 · 深圳市人工智能产业协会

### Part 6: 封底

#### Slide 23 - 封底

- **Layout**: Single column centered + 深蓝渐变背景
- **Title**: 携手高力国际,让 AI 成为商业地产增长新引擎
- **Info**: 深圳市法本信息技术股份有限公司 · FarAI 人工智能解决方案 · 联系方式(待补充)

---

## X. Speaker Notes Requirements

- **Filename**: 匹配 SVG 名(如 `01_cover.svg` → `notes/01_cover.md`)
- **Total duration**: 约 25-30 分钟
- **Notes style**: 正式(formal)+ 适度对话感,适合当面汇报
- **Purpose**: persuade(说服客户认可方案价值)+ inform(讲清四大场景)
- **Content**: 每页脚本要点 + 时间提示 + 过渡话术

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>` 元素
3. 文字换行用 `<tspan>`(禁止 `<foreignObject>`)
4. 透明度用 `fill-opacity`/`stroke-opacity`(禁止 `rgba()`)
5. 禁止:`mask`、`<style>`、`class`、`foreignObject`、`textPath`、`animate*`、`script`
6. 文字字符用原始 Unicode(— – © ® → 等);禁止 HTML 实体(`&nbsp;` `&mdash;` 等);XML 保留字需转义(`&amp;` `&lt;` `&gt;`)
7. 图标用 `<use data-icon="tabler-outline/<name>" .../>` 占位符

### PPT Compatibility Rules:

- 禁止 `<g opacity="...">`(组透明度);在每个子元素上单独设置
- 图片透明度用遮罩层(`<rect fill="bg-color" opacity="0.x"/>`)
- 仅内联样式;禁止外部 CSS 和 `@font-face`
