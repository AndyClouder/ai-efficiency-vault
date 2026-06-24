# 执行者通用规范(Executor Base)

> 把已确认的图类型 + 要素清单 + 视觉规格，逐张手绘成 SVG。本文件是通用规范；具体图类型的构图骨架在 `diagram-types/<type>.md`。

---

## 1. 开工前的强制读取

每张图画完前，确认已读：

| 文件 | 何时读 |
|---|---|
| `references/shared-standards.md` | 第一张图前读一次(全批共用) |
| `references/diagram-types/<本图类型>.md` | 每种用到的新类型读一次 |
| `templates/charts/<相关模板>.svg` | 需要参考成熟实现时读(可选) |
| `<project_path>/spec_lock.md` | **每张图前重读**(强制，防漂移) |
| `<project_path>/analysis.md` | **每张图前重读**(强制，确认要素齐全) |

> 为什么要重读 spec_lock / analysis：长上下文压缩会让模型"忘记"锁定的颜色或漏掉实体。重读是抵抗漂移的硬手段。

---

## 2. 设计参数确认(第一张图前，强制输出)

第一张图前，在聊天里输出一次：

```markdown
📝 **设计参数**
- 画布：1280×720
- 配色：主色 #1E3A5F / 底色 #F8FAFC / 强调 #D4AF37 / 正文 #0F172A
- 字体：-apple-system, ... 'Microsoft YaHei', sans-serif
- 正文字号：14px
- 图标：字母占位
```

防止规格与执行漂移。

---

## 3. 逐图工作流

每张图按这个顺序：

### 3.1 重读 spec_lock + analysis

```bash
read_file <project_path>/spec_lock.md
read_file <project_path>/analysis.md
```

定位到本图要画的实体/关系/层级(从 analysis 的对应块)。

### 3.2 选模板参考(可选)

若 `templates/charts/` 有相近模板(查 [`diagram-types/<type>.md`](diagram-types/_index.md) 的"参考模板"字段)，读它一次。**模板只提供结构骨架**：节点怎么排、连线怎么走、标签放哪。**颜色/字体必须重绘为 spec_lock 的值**，禁止直接复制模板的 HEX。

### 3.3 布局规划(写在聊天里，再画)

```markdown
📐 **图N 布局规划**(<type>)
- 画布：1280×720
- 节点：[列出要画的节点及其大致坐标区]
- 连线：[列出连线及其方向]
- 参考模板：layered_architecture.svg(取其三层堆叠结构)
```

简短即可，目的是把脑中布局落成文字，避免画歪。

### 3.4 手绘 SVG

逐张手写到 `<project_path>/svg_output/<NN>_<type>.svg`：

- `NN` = 图序号(01, 02, …)
- `<type>` = 图类型(architecture / flowchart / sequence / …)
- 文件头必须有 `xmlns`、`viewBox`、`width`、`height`(见 shared-standards §5.1)

> ⚠️ **主代理专用，逐张手绘**：禁止用脚本批量生成 SVG；禁止委托子代理画图。跨图视觉一致性依赖逐张创作 + 上游上下文。

### 3.5 自检(每张图后)

对照 [`shared-standards.md`](shared-standards.md) §8 的自检清单逐项核对。发现问题立刻改，改完再画下一张。

---

## 4. 节点/连线/标签的通用画法

### 4.1 节点卡片(最常用)

```xml
<g filter="url(#cardShadow)">
  <rect x="114" y="184" width="220" height="82" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
  <rect x="126" y="198" width="36" height="36" rx="8" fill="#EFF6FF"/>
  <text x="144" y="222" text-anchor="middle" font-family="..." font-size="16" font-weight="800" fill="#1E3A5F">U</text>
  <text x="174" y="214" font-family="..." font-size="15" font-weight="700" fill="#0F172A">用户服务</text>
  <text x="174" y="234" font-family="..." font-size="12" font-weight="600" fill="#94A3B8">User Service</text>
  <line x1="126" y1="244" x2="322" y2="244" stroke="#F1F5F9" stroke-width="1"/>
  <text x="126" y="258" font-family="..." font-size="11" fill="#475569">用户域业务逻辑</text>
</g>
```

要素：
- 外层 `<g>` 套 `filter="url(#cardShadow)"`(阴影，defs 见 shared-standards §3)
- `<rect>` 主体：白底 + 浅灰描边 + `rx="8"` 圆角
- 左上角字母图标：小方块 + 首字母
- 标题 + 副标题(中英双语或单语)
- 分隔线 + 一行说明

### 4.2 容器/分组

把多个节点圈进一个语义组(如"应用层""服务层")：

```xml
<rect x="96" y="140" width="950" height="140" rx="12" fill="#EFF6FF" fill-opacity="0.6" stroke="#93C5FD" stroke-width="1.5" stroke-dasharray="6 4"/>
<text x="571" y="166" text-anchor="middle" font-family="..." font-size="13" font-weight="700" fill="#1E3A5F" letter-spacing="1">应用层 · APPLICATION LAYER</text>
```

要素：半透明底色 + 虚线描边 + 顶部层标题(小号大写字距加宽)。

### 4.3 连线

**普通连线(无箭头)**：
```xml
<line x1="220" y1="100" x2="220" y2="180" stroke="#64748B" stroke-width="2"/>
```

**带箭头(调用/请求/数据流)**：
```xml
<line x1="100" y1="200" x2="400" y2="200" stroke="#1E3A5F" stroke-width="2.5" marker-end="url(#arrowHead)"/>
```

**连线带标签(时序图/数据流)**：在线条上方/下方放一个小药丸标签：
```xml
<line x1="380" y1="250" x2="900" y2="250" stroke="#1E3A5F" stroke-width="2.5" marker-end="url(#arrowHead)"/>
<rect x="500" y="234" width="280" height="26" rx="11" fill="#FFFFFF" stroke="#1E3A5F" stroke-width="1"/>
<text x="640" y="251" text-anchor="middle" font-family="..." font-size="13" font-weight="700" fill="#1E3A5F">① 登录请求 · POST /auth/login</text>
```

> **每条带方向的连线都必须有标签**或能从上下文明确含义。禁止画"光秃秃的箭头"(不知道表示什么)。

**正交折线(转弯连线)**：用 `<path>` 而非多个 `<line>`，避免接头处错位：
```xml
<path d="M 400 250 L 600 250 L 600 400 L 800 400" fill="none" stroke="#1E3A5F" stroke-width="2.5" marker-end="url(#arrowHead)"/>
```

---

## 5. 多图一致性

若一批要画多张图，保持：

- **配色一致**：全部来自同一 spec_lock
- **节点风格一致**：同种语义的节点(如"服务")在所有图里画法相同(同形状/同尺寸/同字号)
- **图标一致**：同一实体在不同图里用同一字母图标(U = 用户服务，到处都是 U)
- **标题栏一致**：每张图顶部标题区画法统一(主标题 + 副标题 + 色条)

---

## 6. 完成判定

每张图同时满足才算完成：
1. SVG 文件已写入 `svg_output/<NN>_<type>.svg`
2. shared-standards §8 自检清单全过
3. analysis.md 中本图的实体/关系/层级全部出现在图上(无遗漏)
4. 连线方向与 analysis §2 关系表一致

全部图完成后，输出 Step 5 的 Checkpoint。
