# FDE 经分会汇报 - Design Spec

> 面向公司经分会的 FDE（前沿部署工程师）认知拉齐汇报。结论先行（pyramid），FarAI 品牌视觉（深蓝+圆角卡片），纯图标驱动。
> 机器可读执行契约见 `spec_lock.md`；二者冲突以 `spec_lock.md` 为准。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | FDE 经委会汇报 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 26 页（21 内容页 + 5 章节封面；2026-08-14 增补四阶段人才页） |
| **Design Style** | FarAI 品牌：mode=pyramid + visual_style=soft-rounded |
| **Target Audience** | 公司经分会（非技术背景领导为主） |
| **Use Case** | 内部经分会汇报——FDE 认知拉齐 + 稳妥推进方向 |
| **Created Date** | 2026-08-12 |

**一句话立意**：FDE 是高销毛的新兴业务，但它本质是「一个一个看病」的现场能力——值钱在人、难也在人；我们要战略重视、节奏稳妥、人才优先。

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px，上下 50px |
| **Content Area** | 安全区 1160×620；标题区 1160×90；正文区 1160×500；页脚 1160×30 |

---

## III. Visual Theme

### Theme Style

- **Mode**: `pyramid`（结论先行，每页一个核心信息，决策支持标配）
- **Visual style**: `soft-rounded`（圆角卡片 rx12，企业产品风，亲和专业）
- **Theme**: Light theme（白底为主，章节封面/封面用深蓝渐变）
- **Tone**: 专业、稳重、克制；先给判断再给论据；痛点用橙、价值用绿、品牌用蓝

### Color Scheme（FarAI 品牌色，锁定）

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 页面背景 |
| **Secondary bg** | `#F4F7FC` | 卡片背景/分区背景 |
| **Primary** | `#0052A6` | 品牌主色：标题装饰、关键区块、图标主色（FarAI 深蓝） |
| **Accent** | `#246BFE` | 数据高亮、强调亮蓝 |
| **Secondary accent** | `#518FEC` | 次级强调、渐变过渡 |
| **Body text** | `#25364A` | 正文（深） |
| **Secondary text** | `#5E6A78` | 正文（灰）、注释 |
| **Tertiary text** | `#6B7785` | 辅助信息、页脚 |
| **Border/divider** | `#E3E9F2` | 卡片边框、分隔线 |
| **Success** | `#0E9F6E` | 正向指标（价值、达成） |
| **Warning** | `#F59E0B` | 痛点、风险、注意事项 |
| **Info** | `#20A7B8` | 辅助分类（青） |

**深色页辅助色**（封面/章节封面用）：chapter_bg_dark `#0A2A5E`、chapter_bg_mid `#0E367A`、chapter_bg_dark2 `#17365D`、text_on_dark `#FFFFFF`、text_on_dark_secondary `#B8C7E0`、text_on_dark_tertiary `#8FA3C4`、text_on_primary_light `#DCE6FB`。

**配色规则**：60-30-10（白底/浅蓝灰 60% + 品牌蓝 30% + 强调色 10%）；每页不超 4 色；痛点橙、价值绿、品牌蓝有语义不可混用。

### Gradient Scheme（深色页用）

```xml
<linearGradient id="coverBg" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#0A2A5E"/><stop offset="60%" stop-color="#0E367A"/><stop offset="100%" stop-color="#17365D"/>
</linearGradient>
<linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#246BFE"/><stop offset="100%" stop-color="#518FEC"/>
</linearGradient>
<radialGradient id="bgDecor" cx="85%" cy="15%" r="50%">
  <stop offset="0%" stop-color="#246BFE" stop-opacity="0.22"/><stop offset="100%" stop-color="#246BFE" stop-opacity="0"/>
</radialGradient>
```

> 无 AI 图片，故无 AI Image Strategy 段。

---

## IV. Typography System

### Font Plan

**Typography direction**: FarAI concord 同族——微软雅黑贯穿，靠字重（Bold/SemiBold/Regular）拉开层级，PPT-safe 零降级。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:
- Title: `"Microsoft YaHei", Arial, sans-serif`
- Body: `"Microsoft YaHei", Arial, sans-serif`
- Emphasis: same as Body（靠 Bold/SemiBold 字重区分）
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 18px（信息密度高，经分会方案每页 4-8 要点）

| Purpose | px | Weight |
| ------- | --- | ------ |
| Cover title | 56 | Bold |
| Chapter number（装饰） | 220 | Bold, opacity 0.22 |
| Chapter title | 40 | Bold |
| Page title | 30 | Bold |
| Hero number | 32 | Bold |
| Subtitle | 24 | SemiBold |
| **Body** | **18** | Regular |
| Annotation | 14 | Regular |
| Page number | 11 | Regular |

**公式策略**: `text-only`（无公式渲染需求）

---

## V. Layout Principles

### Page Structure

- **Header area**: 高 90px——章节小标签（14px 蓝）+ 主标题（30px 深蓝 Bold）+ 副标（16px 灰）
- **Content area**: 高 500px——卡片网格/流程/图表主体
- **Footer area**: 高 30px——左下"©法本信息版权所有"（11px 灰）+ 右下页码

### Layout Pattern Library

四版式范式（FarAI）：
1. **封面页**：深蓝渐变 + 左侧色块条 + 56px 大标题 + 品牌标识
2. **章节封面页**：深蓝渐变 + 220px 半透明章节号 + CHAPTER N + 40px 章节标题
3. **内容页**：顶部章节标签 + 主标题 + 卡片网格（2×2/三列/四列，rx12 圆角，#F4F7FC 底，顶部色块条）
4. **流程/闭环页**：等宽圆角节点 + marker-end 箭头串联

**卡片变体**：痛点卡（左侧 4px 橙竖条）/ 能力卡（顶部色块条+药丸标签）/ 价值卡（hero_number 大数字）。

### Spacing Specification

**Universal**: 安全边距 50px｜内容块间距 28px｜图标-文字间距 12px
**Card-based**: 卡片间距 24px｜卡片内边距 24px｜圆角 rx12｜三列卡宽 360px｜双行卡高 280px

---

## VI. Icon Usage Specification

### Source

- **Library**: `tabler-outline`（线框、专业、企业感），全篇唯一库，stroke-width=2
- **Usage**: `<use data-icon="tabler-outline/<name>" x="" y="" .../>`，始终 `fill="#HEX"`，绝不用 stroke

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| AI/智能 | `tabler-outline/brain` | 封面、P7、P23 |
| 人才/团队 | `tabler-outline/users` | P12、P21、P22 |
| 风险/警示 | `tabler-outline/alert-triangle` | P12、P14、P15 |
| 目标/价值 | `tabler-outline/target` | P9、P22 |
| 数据/分析 | `tabler-outline/chart-bar` | P9、P10 |
| 流程箭头 | `tabler-outline/arrow-right` | P4、P17、P19 |
| 闭环/沉淀 | `tabler-outline/refresh` | P4、P18 |
| 完成/达成 | `tabler-outline/circle-check` | P9、P25 |
| 灯泡/洞察 | `tabler-outline/bulb` | P5、P23 |
| 路径/路线 | `tabler-outline/route` | P17、P19、P25 |
| 现金/成本 | `tabler-outline/cash` | P9、P18 |
| 报告/文件 | `tabler-outline/file-text` | P3、P13 |
| 搜索/发现 | `tabler-outline/search` | P3、P17 |
| 工厂/行业 | `tabler-outline/building-factory` | P5、P15 |
| 学校/教育 | `tabler-outline/school` | P19 |
| 证书/认证 | `tabler-outline/certificate` | P19、P21 |
| 上升趋势 | `tabler-outline/trending-up` | P8、P10 |

> Executor 实际使用前用 `ls templates/icons/tabler-outline/ | grep <keyword>` 校验文件名存在性。

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P03 | labeled_card | `templates/charts/labeled_card.svg` | "Pick for 3-4 parallel aspects of one subject with per-aspect titles + short body (self-introduction, four-pillar overview, capability quadrant). Skip for plain feature lists (use icon_grid), sequential steps (use numbered_steps), or strategic quadrants (use quadrant_text_bullets / matrix_2x2)." | 三种角色（咨询/外包/FDE）做法并列对比 |
| P04 | pyramid_chart | `templates/charts/pyramid_chart.svg` | "Pick for 3-6 stratified hierarchy layers in flat 2D side-view — Maslow's hierarchy, maturity models, value hierarchy, capability tiers, market segments, audience pyramid. Skip for dramatic tone (use pyramid_isometric), flat priority list (use vertical_list), or org reporting (use top_down_tree)." | FDE 试金石四级（外包→项目制→FDE→可规模化）层级递进 |
| P07 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases. Skip if steps need connector arrows (use process_flow) or named output artifacts (use pipeline_with_stages)." | 80/95/99 三档覆盖率递进，强调数字 |
| P09 | kpi_cards | `templates/charts/kpi_cards.svg` | "Pick for 4-8 standalone numeric metrics shown as overview cards (2x2 or 1x4) — exec summary opener, dashboard headline, quarterly recap, results-at-a-glance. Skip if metrics have target baselines (use bullet_chart) or single hero number (use gauge_chart)." | Palantir 82% 毛利 + 国内百万级付费等销毛数据 |
| P12 | vertical_pillars | `templates/charts/vertical_pillars.svg` | "Pick for 1×3 / 1×4 / 1×5 vertical column layout where each pillar = one independent category with title + bullets — PEST (Political/Economic/Social/Technological), four-pillar strategy overview, side-by-side independent categories. Skip for 2×2 quadrant (use quadrant_text_bullets), pricing tiers (use comparison_columns), or 2×2 parallel aspects (use labeled_card)." | 领导定调的三大风险并列（新兴行业/人才/客户） |
| P13 | comparison_table | `templates/charts/comparison_table.svg` | "Pick for 2-4 plans/products compared across many feature rows (dense matrix). Skip for pricing-tier marketing layout (use comparison_columns)." | 硅谷 vs 国内多维度对比（客单价/数据/投入/人才） |
| P14 | icon_grid | `templates/charts/icon_grid.svg` | "Pick for 4-9 parallel features/capabilities/services as icon cards — feature grid, service lineup, benefits matrix, brand values, product highlights. Skip for sequential ordering (use numbered_steps) or hierarchical layers (use pyramid_chart)." | 五大系统性风险图标网格 |
| P17 | process_flow | `templates/charts/process_flow.svg` | "Pick for 3-8 sequential steps connected by simple arrows — approval workflows, customer onboarding, request handling, lifecycle stages. Skip if cyclical (use circular_stages) or stages produce named outputs (use pipeline_with_stages)." | 一线四步打法（理解→搭建→质量→验证） |
| P18 | timeline | `templates/charts/timeline.svg` | "Pick for 3-8 milestone events on a horizontal time axis (no duration). Skip for tasks with start/end ranges (use gantt_chart) or vertical layout (use roadmap_vertical)." | 本体沉淀复利账（第1→8 客户成本/毛利演变） |
| P19 | chevron_process | `templates/charts/chevron_process.svg` | "Pick for 3-6 phase methodology with chunky arrow-chain progression and deliverables per phase. Skip for <=2 phases or non-linear flow (use process_flow), or chain ending in an aggregate outcome wedge (use chevron_chain_with_tail)." | 推进节奏（原厂打样→沉淀→伙伴复制） |

**Runners-up considered**:

- `vertical_list` | rejected for P12：三条风险是并列的三大独立类别，vertical_pillars 的三列并排视觉冲击更强；vertical_list 纵向编号更适合线性递进而非并列警示
- `numbered_steps` | rejected for P17：四步打法步骤间有明确协作迭代关系（理解→搭建→质量→验证），process_flow 的箭头连接更能表达流转；numbered_steps 更适合无连接的并列步骤
- `roadmap_vertical` | rejected for P18：复利账是横向时间演进（第1→8 客户），timeline 横向更适合 16:9 画布；roadmap_vertical 纵向里程碑更适合进度跟踪
- `bar_chart` | rejected for P09：销毛数据是几个异质独立指标（毛利率/转化率/客单价），非同类别值比较；kpi_cards 独立数字卡更贴切

---

## VIII. Image Resource List

**无图片资源**——本汇报纯图标 + 数据可视化驱动（image_usage = none），跳过 Step 5 图片生成。所有视觉由 tabler-outline 图标 + SVG 原生图形 + FarAI 卡片网格承载。

---

## IX. Content Outline

> 五段式辩证主线：是什么（P2-5）→ 机会与销毛（P6-10）→ 真相与风险（P11-15）→ 稳妥路径（P16-19）→ 人才与组织（P20-23）→ 收尾（P24-25）。情绪曲线：兴奋→清醒（重头）→踏实→安心。

### 开场

#### Slide 01 - 封面/定调
- **Layout**: 封面页（深蓝渐变 + 左侧色块条 + 大标题）
- **Title**: FDE：AI 落地的「最后一公里」
- **Subtitle**: 值钱在人，难也在人——战略重视 · 节奏稳妥 · 人才优先
- **Core message**: 用 25 分钟把 FDE 讲清楚——它是什么、为什么是机会、为什么不能急、我们怎么稳妥做。
- **Info**: 法本信息 ｜ 2026-08-12 ｜ 经分会汇报

### Part 1：FDE 到底是什么

#### Slide 02 - 章节封面①
- **Layout**: 章节封面（深蓝渐变 + 220px 半透明"01"）
- **Title**: CHAPTER 01 ｜ FDE 到底是什么
- **Subtitle**: 不是外包、不是咨询，是「现场解决问题 + 沉淀资产」

#### Slide 03 - 同一个客户，三种角色三种做法
- **Layout**: 三列卡片（labeled_card）
- **Title**: 咨询、外包、FDE，解决的是不同层面的问题
- **Core message**: FDE 不是高级咨询，也不是驻场外包换个名字——它第一周就在改模型。
- **Visualization**: labeled_card（P03）
- **Content**（银行信贷自动化案例）:
  - 咨询顾问：待两周出 80 页 PPT，画路线图，然后走了
  - 外包工程师：等需求文档，按文档写代码，上线收尾款，撤了
  - FDE：坐到风控经理旁边，第一周改模型，还把问题反馈给产品团队

#### Slide 04 - FDE 的本质：交付完留下资产
- **Layout**: 四级金字塔（pyramid_chart）
- **Title**: 判断是不是 FDE，看项目结束后留下了什么
- **Core message**: 买的是结果，不是时间——只留系统是外包，沉淀为可复用资产才是 FDE。
- **Visualization**: pyramid_chart（P04）
- **Content**（试金石四级，自下而上）:
  - 只留一个系统 = 外包
  - 带回经验但无法复用 = 项目制
  - 沉淀为可复用能力（Skill/模板）= FDE
  - 沉淀后让下一个客户更便宜 = 可规模化的 FDE

#### Slide 05 - 警惕「假 FDE」
- **Layout**: 左右对比（伪 FDE vs 真 FDE）
- **Title**: 带产品找问题 ≠ 现场解决问题
- **Core message**: 很多公司只是「把员工扔到一线」，FDE 的本质是接近创业的能力。
- **Content**:
  - 反例：某协同办公团队进工厂，第一件事装摄像头抓抽烟——既不核心又没门槛
  - 真 FDE：到现场重新看业务，找产品良率、订单延期这些真问题
  - ABC 满天飞，但「FDE 就死了」——概念泡沫要警惕

### Part 2：机会与销毛潜力

#### Slide 06 - 章节封面②
- **Layout**: 章节封面（220px 半透明"02"）
- **Title**: CHAPTER 02 ｜ 为什么现在火，机会与销毛潜力在哪
- **Subtitle**: 不是炒概念，是 AI 落地深水区的结构性必然

#### Slide 07 - AI 落地进入「深水区」
- **Layout**: 三档递进（numbered_steps）
- **Title**: 不缺 Demo，缺把 AI 真正跑进业务的人
- **Core message**: 矛盾从「模型能不能做」转向「组织怎么用」，95→99% 才是 FDE 的战场。
- **Visualization**: numbered_steps（P07）
- **Content**（80/95/99 规律）:
  - 0→80%：通用大模型 + 简单 Prompt，一天就能搭出「挺好用」的原型
  - 80→95%：行业术语、边界情况，需 Prompt/规则/数据/测试集，很难
  - 95→99%：1% 错误可能致严重后果，才是 FDE、专用平台和万级真实数据的战场
  - >60% 企业 AI 尝试仍停在试点阶段

#### Slide 08 - 为什么现在才可行
- **Layout**: 三列卡片（三道成本闸门）
- **Title**: AI 打开了三道成本闸门，过去「不划算」的重交付重新可行
- **Core message**: 可编码的经验正在廉价化，不可编码的洞察正在稀缺化。
- **Content**（三项成本同时下降）:
  - 行业知识蒸馏成本 ↓：一线能现场写脚本、封装工具、搭原型
  - 定制开发成本 ↓：小团队即可完成价值验证
  - 复合型人才供给成本 ↓：AI 补齐部分工程/文档/产品能力

#### Slide 09 - 高销毛是真的
- **Layout**: KPI 数据卡（kpi_cards）
- **Title**: 不是只讲故事的赔本买卖，有真实的高毛利逻辑
- **Core message**: 标杆毛利 82%，国内已有真金白银验证 FDE 可独立定价。
- **Visualization**: kpi_cards（P09）
- **Content**:
  - Palantir 毛利率约 82%（接近纯软件公司，远高于咨询业 30-40%）
  - Bootcamp 5 天驻场，转化率 70%、获客成本降 40-60%
  - 国内：腾讯云 FDE 服务已被验证可独立定价，头部客户百万–五百万级
  - 收入逻辑：席位费只是入口，客户持续使用产生的消耗才是长期引擎

#### Slide 10 - 趋势已经起来
- **Layout**: 三趋势信号（vertical_list）
- **Title**: 招聘、大厂、政策三重信号——不是我们在追风口
- **Core message**: FDE 已成行业共识，角色还在升级（FDE→FDX「外置 CEO」）。
- **Content**:
  - 招聘：海外 FDE 岗位一年增长 729%（643→5330），均薪约 19.6 万美元
  - 大厂下场：AWS 投 10 亿美元、OpenAI/Anthropic 直接做企业交付
  - 政策：上海全国首个将 FDE 写入产业政策（2026.1）

### Part 3：真相与风险（重头）

#### Slide 11 - 章节封面③
- **Layout**: 章节封面（220px 半透明"03"）
- **Title**: CHAPTER 03 ｜ 真相与风险
- **Subtitle**: 值钱，但绝不是马上能变现的数字

#### Slide 12 - 清醒剂：领导定调的三条风险
- **Layout**: 三列风险卡（vertical_pillars）
- **Title**: FDE 值钱，但预期管理比打鸡血更重要
- **Core message**: 介绍 FDE 会无限放大期待，反向变成经营压力——这是最大的顾虑。
- **Visualization**: vertical_pillars（P12）
- **Content**（领导原话三条风险）:
  - 新兴行业无规范：业务流程无标准、商业化路径不成熟
  - 人才苛刻到市场招不到：内部转型也需意愿+培训+工具，是长周期
  - 客户门槛高：需客户 IT 成熟度+AI 接受度，需客户侧 FDE 配合，有行业壁垒

#### Slide 13 - 国内现实
- **Layout**: 中美对比表（comparison_table）
- **Title**: 硅谷的赚钱模式，国内还远达不到
- **Core message**: 国内 FDE 和国外「根本不是一回事」，核心挑战是经济性。
- **Visualization**: comparison_table（P13）
- **Content**（硅谷 vs 国内多行对比）:
  - 客单价：硅谷六七位数美元年合同 vs 国内十万–百万人民币
  - 数据底子：美国 ERP/CRM/ITSM 完善沉淀 vs 国内流程写在默契里
  - 标杆投入：Palantir 本体层十余年+数百工程师+0.3% 录用率，国内复制不了
  - 核心挑战就是经济性——账要算得过来

#### Slide 14 - 系统性风险
- **Layout**: 五卡片网格（icon_grid）
- **Title**: FDE 最怕的不是做不成，是做着做着变成「换名字的外包」
- **Core message**: 所有风险本质上都指向一个问题——能不能持续降低边际成本。
- **Visualization**: icon_grid（P14）
- **Content**（五大风险）:
  - 本体缺失恶性循环：没沉淀→每单从零→更没时间沉淀
  - 组织归属：放销售/交付/产品体系各有陷阱
  - 落地易扩展难：新鲜感退后使用率降
  - 利润率结构性偏重：价值定价国内有障碍
  - 模型厂商既是伙伴也是潜在竞争者

#### Slide 15 - 概念泡沫
- **Layout**: 警示清单（vertical_list）
- **Title**: 很多 FDE 是「挂羊头」
- **Core message**: 国内大量岗位挂 FDE 名，实质还是实施/部署/培训。
- **Content**:
  - 中美差距：岗位认知易与驻场外包混淆、组织授权不足、产品沉淀弱
  - 从业者类比「十年前的产品经理」——窗口期 5-10 年，但会大浪淘沙
  - 我们要做真 FDE、不做伪 FDE

### Part 4：怎么稳妥推进

#### Slide 16 - 章节封面④
- **Layout**: 章节封面（220px 半透明"04"）
- **Title**: CHAPTER 04 ｜ 怎么稳妥推进
- **Subtitle**: 先验证、先沉淀、先打标杆

#### Slide 17 - 验证方法论
- **Layout**: 四步流程（process_flow）
- **Title**: 先证明价值，再谈规模
- **Core message**: 卖成果，不卖软件——客户为业务真的变好付费。
- **Visualization**: process_flow（P17）
- **Content**（一线四步打法）:
  - 业务理解：钱从哪来、卡在哪、AI 撬哪
  - 协作搭建：业务专家+FDE 共建 Agent/工作流
  - 质量保障：真实数据生成测试集 + 自动评测 + A/B
  - 结果验证：AI 组 vs 人工组逐环节对比
  - 多数项目死在试点→生产之间（数据质量被回避、审批未打通）

#### Slide 18 - 沉淀逻辑：一笔复利账
- **Layout**: 横向时间线（timeline）
- **Title**: 先投入、后回收——FDE 能不能赚钱，看会不会把经验变成资产
- **Core message**: 冷启动约 150 万，第 8 个客户累计节省约 300 万，正式回本。
- **Visualization**: timeline（P18）
- **Content**（本体沉淀五阶段，第1→8 客户）:
  - 第 1 客户：成本是从零定制的 3 倍，毛利率 25%
  - 第 4 客户：Delta 工时降至 4 人天，本体迭代到 V1.3
  - 第 5-8 客户：上线周期 6 周→1 周，毛利率 55%→70%
  - 第 8 客户累计节省约 300 万，正式回本；7-8 客户后本体趋稳

#### Slide 19 - 推进节奏
- **Layout**: 三阶段箭头链（chevron_process）
- **Title**: 原厂打样、伙伴复制，先易后难
- **Core message**: 0 到 1 原厂、1 到 N 伙伴——部署是「脚手架」不是「房子」。
- **Visualization**: chevron_process（P19）
- **Content**:
  - 原厂打样：重点行业标杆跑通，沉淀 Skill/模板/连接器/方法论
  - 伙伴复制：ISV/SI/区域伙伴规模化交付，平台培训认证
  - 客户自助：逐步形成自助构建能力
  - 行业优先序：先高容错（教育/传媒/文旅），后高精度（工业/金融）

### Part 5：人才与组织

#### Slide 20 - 章节封面⑤
- **Layout**: 章节封面（220px 半透明"05"）
- **Title**: CHAPTER 05 ｜ 人才与组织
- **Subtitle**: 价值在人，瓶颈也在人

#### Slide 21 - 人才策略跟着阶段走：先想能力，不想岗位
- **Layout**: dense（四阶段 chevron + 四卡 + 双视角带）
- **Title**: 人才策略跟着阶段走：先想能力，不想岗位
- **Core message**: 第一步不是「要不要招 FDE」，而是「谁对 AI 落地结果负责」——需要的是一套能力，不是一个岗位名称。
- **Content**:
  - 四阶段：①先借能力（外部 FDE + 内部负责人，跑通第一个项目）→ ②内部孵化（不看原有岗位）→ ③正式招聘（从项目能力到组织能力）→ ④内外协同（复杂大型企业）
  - 客户视角：客户正处在阶段 1–2「先借能力」——正是外部 FDE 服务商（我们）的市场窗口
  - 自身视角：人招不到，就更不能从招聘入手——先借力验证、再内部转型
- **素材**: 新素材《企业FDE人才：招聘还是内部培养》+ PDF 第 8 章（2026-08-14 增补）

#### Slide 22 - 从内部挖人：4 特质选人 + 项目制培养
- **Layout**: dense（4 特质卡 + 培养阶梯 + 警示带）
- **Title**: 从内部挖人：4 特质选人 + 项目制培养
- **Core message**: 市场上几乎招不到——行业 SA、交付、行业专家最接近，选人只看 4 项特质，不看原有岗位。
- **Content**:
  - 4 特质：懂业务 / 能动手实操 / 懂 AI / 对结果负责
  - 培养是项目制不是课堂制：0-3 月基础→9-18 月独立交付→18 月+能定义问题
  - FDE 能力不是培训出来的，是在真实项目里长出来的
  - 警惕「干得好就调回总部」的一线失血陷阱

#### Slide 23 - 人才观：从「把人当资源」到「把人当资产」
- **Layout**: breathing（单一强调，负空间）
- **Title**: 彻底扭转「把人当资源」的旧理念
- **Core message**: 尊重人才、培养人才、吸引人才——让沉淀经验真正算进绩效。
- **Content**:
  - 机制保障：双轨绩效 + 内部结算，让「沉淀/跨客户复用」算绩效
  - 能力越往上越值钱：行业洞察、客户信任、组织推动——AI 替代不了

#### Slide 24 - AI 让判断变稀缺
- **Layout**: breathing（单一强调）
- **Title**: 懂业务、懂组织、懂指挥 AI 的人，不会被取代
- **Core message**: 既要讲 AI 的革新力，也要安抚焦虑——AI 不会取代能驾驭它的人。
- **Content**:
  - AI 让工程执行变便宜，让判断能力更稀缺
  - 前线角色从「写代码的人」→「指挥 AI 完成业务的人」
  - 模型再强，仍需知道行业如何运转、客户如何决策——把知识变成组织资产的人最值钱

### 收尾

#### Slide 25 - 一句话总结：潜力、真相、路径、人才
- **Layout**: breathing（四段收束）
- **Title**: 四句话收束全场
- **Core message**: FDE 值得战略投入，但要战略重视、节奏稳妥、人才优先。
- **Content**:
  - 潜力：AI 落地最后一公里，有真实高销毛逻辑
  - 真相：新兴行业，国内国外不同，难在人、周期长，别变成经营压力
  - 路径：先验证、先沉淀、先打标杆，原厂打样、伙伴复制、先易后难
  - 人才：人才策略跟着阶段走——从「把人当资源」到「把人当资产」，AI 不取代驾驭它的人

#### Slide 26 - 下一步建议
- **Layout**: 三动作卡片
- **Title**: 从「认知拉齐」走向「具体行动」
- **Core message**: 三个起步动作，方向性推进，具体经营方案留后续专题。
- **Content**:
  - 选 1-2 个高容错行业做验证试点（教育/传媒/文旅），跑出标杆
  - 按 4 特质盘人（懂业务/能实操/懂 AI/对结果负责），SA/交付/行业专家最接近，启动转型培养
  - 建机制：把「经验沉淀/跨客户复用」纳入绩效，设 Skill/本体沉淀专项

---

## X. Speaker Notes Requirements

- **Filename**: 匹配 SVG 名（`01_cover.svg` → `notes/01_cover.md`）
- **总时长**: 25-30 分钟
- **风格**: 正式但讲人话（受众是非技术领导），多案例少概念
- **目的**: inform + persuade（认知拉齐 + 争取战略支持 + 管理预期）
- **每页要点**: 核心论点 + 关键数据 + 过渡句；风险段（P11-15）加重语气

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:
1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>`
3. 文字换行用 `<tspan>`（`<foreignObject>` 禁用）
4. 透明度用 `fill-opacity`/`stroke-opacity`；`rgba()` 禁用
5. 禁用：`mask`、`<style>`、`class`、`foreignObject`、`textPath`、`animate*`、`script`、`@font-face`、`<symbol>`+`<use>`（图标 use 占位除外）
6. 文字字符用原生 Unicode（— – © ® → 等）；HTML 实体禁用；XML 保留字转义（`&amp;` `&lt;` `&gt;`）
7. `<g opacity>` 禁用，opacity 设在每个子元素上
8. `marker-start`/`marker-end`：`<marker>` 须在 `<defs>`，`orient="auto"`，形状为三角/菱形/圆

### PPT Compatibility:
- 卡片圆角用 `<rect rx="12">`
- 图标用 `<use data-icon="tabler-outline/...">` 占位（finalize 阶段嵌入）
- 字体栈首字必须预装（微软雅黑/Arial）
