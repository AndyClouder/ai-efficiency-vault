---
name: farai-style-conversion
description: 为 PPT 套用法本 FarAI 品牌视觉规范(深蓝主色 #0052A6 + 微软雅黑 + 圆角卡片 + pyramid 结论先行),生成可直接交给 ppt-master 的 spec_lock.md 与 design_spec 风格段。触发场景:用户说"套 FarAI 风格""法本品牌色""用 FarAI 做 PPT""FarAI 风格""法本 PPT 风格",或在售前 PPT 制作中需要锁定品牌视觉时。本 skill 只产出风格规范,不生成 SVG/PPTX。
---

# FarAI 风格转化器

> 法本信息 FarAI 品牌视觉规范的固化载体。把"配色/字体/字号/版式"四大要素锁定为可执行的 spec_lock,作为 ppt-master 的前置风格插件。

---

## 触发条件

- 用户说:"套 FarAI 风格" "法本品牌色" "用 FarAI 做 PPT" "FarAI 风格" "法本 PPT 风格"
- 用户说:"用我们公司的品牌色" "法本红/法本蓝"(识别到法本/Farben 语境)
- 在售前 PPT / 汇报 PPT 制作流程中,需要锁定品牌视觉时(通常由「售前 PPT 编写」skill 调用)
- 用户键入:`/farai风格` `/法本风格`

**与 ppt-master 的边界**:本 skill 只产风格规范(spec_lock.md + design_spec 风格段),**不生成 SVG、不导出 PPTX**。物理生成交给 ppt-master。
**与售前 PPT 编写的边界**:售前 skill 是总指挥,本 skill 是它调用的"风格工具"。单独触发本 skill 时,产出风格规范即可,不必驱动整个售前流程。

---

## 工作流程

### 第一步:加载 FarAI 品牌规范

读取 `references/farai-brand-spec.md`,掌握四大要素:

1. **配色**(12 个角色 HEX,含深色页辅助色)
2. **字号 ramp**(基于 body=18px 的 9 级锚点)
3. **字体与图标**(`"Microsoft YaHei", Arial, sans-serif` + tabler-outline 图标库)
4. **版式范式**(封面/章节封面/内容页/流程页 四种,每种含布局骨架)

### 第二步:按 PPT 用途给版式建议

根据用户 PPT 的页面构成,对照版式范式给出建议:

| 页面类型 | 推荐版式 | 核心要点 |
|---------|---------|---------|
| 封面 | 深蓝渐变 + 左侧色块 + 大标题 | 巨型标题(56px)+ 副标 + 品牌标识 + 底部公司信息 |
| 章节封面 | 深蓝渐变 + 巨型半透明章节号 | 220px 半透明章节数字 + CHAPTER N + 章节标题(40px) |
| 内容页 | 顶部章节标签 + 主标题 + 卡片网格 | 2×2 矩阵 / 三列 / 四列卡片,卡片 rx12 圆角,标题色块 |
| 流程/闭环页 | 横向箭头串联等宽节点 | 等宽圆角节点 + marker-end 箭头 + 闭环虚线回流 |

若用户已有大纲,逐页匹配版式;若无,给出 FarAI 风格下推荐的 23 页标准结构。

### 第三步:生成 spec_lock.md 骨架

读取 `references/spec-lock-template.md`,它是预填了 FarAI 全部默认值的 spec_lock 骨架。只需:

1. 替换 `project_name` 为实际项目名
2. 填入 `page_rhythm`(每页的 anchor/dense/breathing 节奏)
3. 按需补充 `page_charts`(若有流程图/中心辐射等图表页)

产出物保存到 ppt-master 项目目录:`projects/<project_name>_ppt169_<date>/spec_lock.md`

### 第四步:交接给 ppt-master

告诉用户:
> FarAI 风格已锁定,spec_lock.md 已生成在 `<路径>`。接下来调用 **ppt-master** skill,它会读取此 spec_lock 逐页生成 SVG 并导出 PPTX。

若在售前 PPT 编写流程内被调用,则直接把 spec_lock 路径返回给调用方,由售前 skill 继续驱动 ppt-master。

---

## 与 ppt-master 的协作契约

本 skill 在 ppt-master 流水线中的介入点:

| ppt-master 阶段 | 本 skill 的动作 |
|----------------|----------------|
| Step 2 项目初始化后 | 提供 FarAI 品牌色/字体/版式,影响 design_spec.md 的 §III 视觉主题、§IV 字体、§V 布局 |
| Step 3 模板选项 | **跳过模板查询**——FarAI 是已知风格,直接走 free design + 风格锁定 |
| Step 4 Strategist 八项确认 | 预填八项的推荐值(画布16:9 / pyramid / soft-rounded / FarAI色 / tabler-outline / 微软雅黑 / 无图),让用户只需确认 |
| Step 4 输出 spec_lock.md | **直接套用 spec-lock-template.md**,无需 Strategist 从零推导 |

**关键**:FarAI 风格下的 mode 固定为 `pyramid`(结论先行,售前决策支持标配),visual_style 固定为 `soft-rounded`(圆角卡片,企业产品风)。这两个值已写进 spec-lock-template.md。

---

## 注意事项

1. **仅限 FarAI 品牌**——本 skill 的色值/字号/版式是法本 FarAI 专属,不可私自改成其他品牌。若用户要其他品牌风格,提示走 ppt-master 的 free design 自定义。
2. **spec_lock 是执行契约**——产出的 spec_lock.md 会被 ppt-master 在每页生成前重读,色值/字号/图标必须与 `references/farai-brand-spec.md` 完全一致,不可临场发挥。
3. **字号遵循 ramp**——所有字号必须是 spec_lock 中 ramp 的锚点或锚点间的插值(比例 1.5-2x 等),不可超出 ramp 区间自创字号。
4. **四镜像同步**——本 skill 修改后,四个目录的 SKILL.md 必须一致:`0_系统配置/.agents/skills/` + `0_系统配置/.claude/skills/`(配置源)+ `.agents/skills/` + `.claude/skills/`(运行时)。references 子目录文件也需同步(虽 pre-commit 钩子只校验 SKILL.md)。
5. **不生成 SVG/PPTX**——本 skill 的产出止于 spec_lock.md(可选加 design_spec 风格段)。物理 PPT 生成交给 ppt-master,避免职责重叠。

---

## 与其他 skill 的协作

| 协作对象 | 关系 | 触发时机 |
|---------|------|---------|
| **售前 PPT 编写** | 上游调用方 | 售前 skill 在"风格套用"步骤调用本 skill 产 spec_lock |
| **ppt-master** | 下游执行者 | 本 skill 产出 spec_lock 后,由 ppt-master 走完 SVG 生成+质检+导出 |
| **图绘大师** | 平行(独立) | 图绘大师是 SVG 手绘,不走 ppt-master 流水线,风格独立 |

---

## 触发示例

**示例 1(单独触发)**:
> 用户:"用法本品牌色做个测试 PPT"
> 本 skill:加载 FarAI 规范 → 给出版式建议 → 生成 spec_lock 骨架 → 提示调用 ppt-master 生成

**示例 2(售前流程内调用)**:
> 售前 skill:"高力国际售前 PPT 内容已规划完毕,需要套 FarAI 风格"
> 本 skill:套用 spec-lock-template → 替换 project_name + 填 page_rhythm → 返回 spec_lock 路径给售前 skill

**示例 3(风格咨询)**:
> 用户:"FarAI 的主色是什么?"
> 本 skill:读 farai-brand-spec.md → 回答 `#0052A6`(品牌主色)+ `#246BFE`(强调色)+ 给出使用场景
