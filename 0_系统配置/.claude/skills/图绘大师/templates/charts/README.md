# SVG 模板库

> 15 个手绘 SVG 模板，源自 ppt-master(`templates/charts/`)，2026-06 对齐。本技能聚焦"架构/系统/流程"类图，故只选了这一子集。

## 用途

这些模板是**结构参考**，不是填空骨架。执行者(Step 5)画图时按需读取：

- 取其**结构骨架**(节点怎么排、连线怎么走、标签放哪)
- 取其**视觉技法**(卡片画法、阴影、箭头、容器框)
- **颜色/字体必须重绘**为当前项目的 `spec_lock.md` 值，禁止直接用模板的 HEX

## 模板清单(按图类型分组)

| 图类型 | 模板文件 | 适用场景 |
|---|---|---|
| architecture(分层架构) | `layered_architecture.svg` | 3 层 + 右侧输出 + 底部基础层 |
| flowchart(流程) | `process_flow.svg` | 横向直线流程 |
|  | `snake_flow.svg` | 蛇形流程(省空间) |
|  | `pipeline_with_stages.svg` | 带阶段分组的 pipeline |
| sequence(时序) | `client_server_flow.svg` | 客户端↔服务端 + 编号交互 |
| mindmap(思维导图) | `mind_map.svg` | 中心 + 多分支辐射 |
| framework(框架) | `hub_spoke.svg` | 中心 + 卫星辐射 |
| component(组件) | `module_composition.svg` | 多模块 + 依赖连线 |
| hierarchy(层级树) | `top_down_tree.svg` | 自顶向下树 + 正交连线 |
| matrix(矩阵) | `matrix_2x2.svg` | 2×2 四象限 + 双轴 |
| cycle(循环) | `circular_stages.svg` | 环形步骤 + 中心 |
| timeline(时间线) | `timeline.svg` | 横向轴 + 上下交替里程碑 |
| comparison(对比) | `comparison_columns.svg` | 左右两栏对应对比 |
|  | `pros_cons_chart.svg` | 优势/劣势两栏 |
| 鱼骨(因果) | `fishbone_diagram.svg` | 问题 + 分类原因刺 |

## 读取约定

执行者画某类图前，看 `references/diagram-types/<type>.md` 末尾的"参考模板"字段，按需读取对应 SVG。**不需要全部读**——多数项目只用 1-2 个模板。

## 与 ppt-master 的同步

若 ppt-master 上游更新了这些模板，本目录需手动同步。检查命令：
```bash
diff <ppt-master>/templates/charts/<file>.svg <本目录>/<file>.svg
```
