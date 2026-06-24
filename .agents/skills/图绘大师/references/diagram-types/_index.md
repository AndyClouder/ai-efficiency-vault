# 图类型库 — 索引

> 12 种结构化图的构图骨架。每种类型描述"图内部怎么布局"：节点怎么排、连线怎么走、标签放哪。类型按图选定——一张图一个主类型，不要混。

## 1. 类型目录(12 种)

| 类型 | 内部构图 | 典型用途 | 参考模板 |
|---|---|---|---|
| [`architecture`](./architecture.md) | 3-5 层水平堆叠，每层并列多个节点 | 系统/软件分层架构、技术栈 | `layered_architecture.svg` |
| [`flowchart`](./flowchart.md) | 3-6 阶段按方向连接，箭头表流向 | 工作流、pipeline、步骤 | `process_flow.svg` / `snake_flow.svg` |
| [`sequence`](./sequence.md) | 顶部角色列 + 纵向时间轴 + 横向交互箭头 | 请求-响应、API 调用、协议交互 | `client_server_flow.svg` |
| [`mindmap`](./mindmap.md) | 中心节点向四周发散，2-3 层分支 | 知识结构、读书笔记、概念展开 | `mind_map.svg` |
| [`framework`](./framework.md) | 中心节点 + 3-6 卫星节点辐射 | 方法论、模型、中心概念 | `hub_spoke.svg` |
| [`component`](./component.md) | 模块卡片 + 依赖连线(可交叉) | 模块依赖、组件关系 | `module_composition.svg` |
| [`data-flow`](./data-flow.md) | 源 → 处理 → 汇，数据用粗箭头 | 数据流向、ETL、信息流 | `pipeline_with_stages.svg` |
| [`hierarchy`](./hierarchy.md) | 树状：根在顶/左，逐层展开 | 组织结构、分类树、上下级 | `top_down_tree.svg` |
| [`matrix`](./matrix.md) | 2×2 或 3×3 网格，两轴有标签 | SWOT、BCG、四象限分析 | `matrix_2x2.svg` |
| [`cycle`](./cycle.md) | 闭环，3-6 步箭头回到起点 | PDCA、飞轮、持续改进 | `circular_stages.svg` |
| [`timeline`](./timeline.md) | 横/纵轴 + 里程碑节点 | 历史、演进、路线图 | `timeline.svg` |
| [`comparison`](./comparison.md) | 左右/上下对称分栏 | 前后、优劣、A/B 对比 | `comparison_columns.svg` / `pros_cons_chart.svg` |

---

## 2. 自动选择表(源材料信号 → 类型)

内容解析师(Step 3)按源材料的**主结构特征**选型：

| 源材料信号 | 类型 |
|---|---|
| 系统/软件分层、技术栈、明显多层 | `architecture` |
| 步骤、工作流、pipeline、有先后 | `flowchart` |
| 请求-响应、API 调用、协议交互、多角色对话 | `sequence` |
| 概念展开、知识结构、读书笔记、发散性内容 | `mindmap` |
| 方法论、模型、中心概念 + 卫星 | `framework` |
| 模块依赖、组件关系、(可交叉的)调用图 | `component` |
| 数据流向、ETL、信息从一处流向多处 | `data-flow` |
| 组织结构、分类树、上下级、族谱 | `hierarchy` |
| SWOT、四象限、2×2、BCG | `matrix` |
| PDCA、闭环、飞轮、持续改进 | `cycle` |
| 历史、演进、路线图、时间序列里程碑 | `timeline` |
| 前后、优劣、A/B、对比 | `comparison` |
| 鱼骨因果(特殊) | 用 `comparison` 的变体或 `flowchart`，参考 `fishbone_diagram.svg` |

---

## 3. 默认画布与长宽比

类型选定后，画布长宽比有偏好(可在 Step 4 由用户覆盖)：

| 类型 | 默认画布 | 长宽比 |
|---|---|---|
| architecture | 1280×720 | 16:9 |
| flowchart(横向) | 1280×720 | 16:9 |
| flowchart(纵向长流程) | 720×1280 | 9:16 |
| sequence | 1280×720 | 16:9 |
| mindmap | 1280×720 或 1080×1080 | 16:9 / 1:1 |
| framework | 1080×1080 | 1:1 |
| component | 1280×720 | 16:9 |
| data-flow(横向) | 1920×720 | 8:3 |
| hierarchy | 1280×720 | 16:9 |
| matrix | 1080×1080 或 1280×720 | 1:1 / 16:9 |
| cycle | 1080×1080 | 1:1 |
| timeline(横向) | 1920×720 | 8:3 |
| comparison | 1280×720 | 16:9 |

---

## 4. 用法

1. Step 3 内容解析师按 §2 自动选择表给出推荐(1-3 个类型)。
2. Step 5 执行者画某类图前，`read_file references/diagram-types/<type>.md` —— 只读用到的类型，多数项目用 1-2 个。
3. 按需 `read_file templates/charts/<参考模板>.svg`(见每类文件末尾的"参考模板"字段)，取其结构骨架，颜色重绘为 spec_lock 的值。

**多种类型并存正常**：一个项目可能要一张架构图 + 一张时序图，各画各的，配色一致即可。
