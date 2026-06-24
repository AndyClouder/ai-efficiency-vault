# SVG 共享技术约束

> 图表 SVG 的通用技术规范。本技能的 SVG 用于浏览器渲染 + 可选导出 PNG/PPTX，因此约束比 ppt-master(纯 PPTX 导出)略宽，但仍有一批硬性禁用项。

---

## 1. 文本字符：必须是合法 XML

SVG 是严格的 XML。两条铁律：

| 字符类别 | 必须形式 | 禁止形式 |
|---|---|---|
| 排版符号(em dash `—`、en dash `–`、`©`、`®`、`→`、`·`、NBSP、全角标点、emoji…) | **原始 Unicode 字符** — 直接写 `—` `→` `·` | HTML 命名实体 — `&mdash;` `&rarr;` `&middot;` `&nbsp;` `&hellip;` 等 |
| XML 保留字符(`&` `<` `>` `"` `'`) | **仅 XML 实体** — `&amp;` `&lt;` `&gt;` `&quot;` `&apos;` | 裸 `&` `<` `>`，如 `R&D`、`error < 5%` |

一个违规字符就让整个文件无效。数字引用(`&#160;`)合法但不鼓励。

> 常见陷阱：
> - `R&D` → 必须写 `R&amp;D`
> - `A < B` → 必须写 `A &lt; B`
> - 省略号 `...` 用原始 `…` 而非 `&hellip;`
> - 箭头用原始 `→` 而非 `&rarr;`

---

## 2. 禁用特性黑名单

以下在生成的 SVG 中**禁止**出现：

| 禁用项 | 说明 | 替代方案 |
|---|---|---|
| `mask` | 蒙版 | 用 `clipPath` 或分层 `rect` + 渐变 |
| `<style>` | 内嵌样式表 | 用元素属性(`fill=` `stroke=`)逐个写 |
| `class` | CSS 选择器属性 | 用属性直接写样式 |
| `<foreignObject>` | 嵌入外部内容 | 纯 SVG 元素 |
| `<symbol>` + `<use>` | 符号复用 | 直接重复绘制(图通常不大) |
| `textPath` | 文字沿路径 | 普通水平/垂直 `<text>` |
| `@font-face` | 自定义字体 | 用系统字体栈 |
| `<animate*>` / `<set>` | SVG 动画 | 静态图 |
| `<script>` / 事件属性 | 脚本与交互 | 静态图 |
| `<iframe>` | 内嵌框架 | — |

### 2.1 条件允许的特性

| 特性 | 允许条件 |
|---|---|
| `marker-start` / `marker-end` | 仅当 `<marker>` 在 `<defs>` 内、`orient="auto"`、形状是三角/菱形/圆、marker fill 与线条 stroke 同色、宽高在 3-15 范围 |
| `clipPath` | 裁剪图片或节点形状时可用，`<clipPath>` 必须在 `<defs>` 内 |
| `<filter>` | 阴影 `feGaussianBlur`+`feOffset`+`feFlood`+`feComposite` 组合可用(见 §3) |
| `<linearGradient>` / `<radialGradient>` | 渐变可用，必须在 `<defs>` 内定义后引用 |

---

## 3. 阴影(推荐模板)

节点卡片的柔和投影用 `<filter>`，标准模板：

```xml
<defs>
  <filter id="cardShadow" x="-15%" y="-15%" width="130%" height="130%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
    <feOffset dx="0" dy="2" result="offsetblur"/>
    <feFlood flood-color="#0F172A" flood-opacity="0.08" result="shadowColor"/>
    <feComposite in="shadowColor" in2="offsetblur" operator="in" result="shadow"/>
    <feMerge><feMergeNode in="shadow"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
```

`stdDeviation` 建议 4-6，`flood-opacity` 建议 0.06-0.10。太重显脏，太轻看不见。

---

## 4. 箭头(推荐模板)

流程/架构图的连线箭头，标准定义：

```xml
<defs>
  <marker id="arrowHead" markerWidth="10" markerHeight="10" refX="9" refY="5"
          orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L10,5 L0,10 Z" fill="#1E3A5F"/>
  </marker>
</defs>
<line x1="100" y1="200" x2="400" y2="200" stroke="#1E3A5F" stroke-width="2.5"
      marker-end="url(#arrowHead)"/>
```

**关键约定**：
- marker 的 `fill` 必须与线条 `stroke` **同色**(导出时箭头继承线色)
- `orient="auto"` 才能沿线方向自动旋转
- 形状只能是三角(`<path d="M0,0 L10,5 L0,10 Z"/>` / `<polygon>`)、菱形(4 顶点闭合)、圆(`<circle>`)；其他形状会被丢弃
- **双向箭头**：定义两个 marker(`arrowHead` + `arrowTail`)，分别挂 `marker-end` 和 `marker-start`

---

## 5. 坐标与布局

### 5.1 viewBox 必须与画布一致

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
```

`viewBox` 的宽高比必须与 `width`/`height` 一致，否则缩放变形。

### 5.2 留白

- 画布四周留 **40-60px** 安全区(标题/节点不贴边)
- 节点之间留 **20-40px** 间距(避免拥挤)
- 连线与节点边缘留 **10-20px**(箭头不被遮挡)

### 5.3 对齐

- 文字用 `text-anchor`(start/middle/end)对齐，不要靠 x 坐标硬凑
- 垂直居中用 `dominant-baseline="middle"` 或人工算 y = 卡片中心 + 字号×0.35
- 同类节点尺寸统一(同层的卡片同宽同高)

---

## 6. 文本

### 6.1 多行文本

SVG 的 `<text>` 不自动换行。多行用多个 `<text>` 或一个 `<text>` + 多个 `<tspan dy="...">`：

```xml
<text x="174" y="214" font-family="..." font-size="15" font-weight="700" fill="#0F172A">节点标题</text>
<text x="174" y="234" font-family="..." font-size="12" fill="#64748B">节点说明第一行</text>
<text x="174" y="250" font-family="..." font-size="12" fill="#64748B">节点说明第二行</text>
```

> 行距建议 = 字号 × 1.4(中文)或 × 1.3(英文)。

### 6.2 长文本处理

- 节点标题：≤ 8 个中文字 / ≤ 14 个英文字符
- 节点说明：每行 ≤ 16 个中文字 / ≤ 28 个英文字符，超出则换行或精简
- 连线标签：≤ 6 个字，超出则精简或用编号(①②③)

### 6.3 字体栈

统一用(已在 spec_lock 锁定)：
```
-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', 'PingFang SC', sans-serif
```
不要在单个元素上换字体。

---

## 7. 颜色规范

### 7.1 只用 spec_lock 的颜色

每张图的所有 `fill` / `stroke` / `stop-color` 必须来自 `spec_lock.md` 的配色表。禁止临时编 HEX。

### 7.2 透明度

用 `fill-opacity` / `stroke-opacity` 控制透明度，不要用 8 位 HEX(`#1E3A5F80`)——部分渲染器不支持。

### 7.3 层次感

- 卡片底：`fill="#FFFFFF"` + 阴影
- 容器/分组：`fill="<次主色>" fill-opacity="0.6"` + 虚线描边(`stroke-dasharray="6 4"`)
- 焦点节点：主色实心 + 强调色细环

---

## 8. 自检清单(每张图画完后逐项核对)

- [ ] XML 合法(`&`/`<`/`>` 已转义，符号用原始 Unicode)
- [ ] 无禁用特性(mask/style/class/foreignObject/symbol+use/textPath/script/animate)
- [ ] viewBox 与 width/height 一致
- [ ] 所有颜色来自 spec_lock.md
- [ ] 字体栈统一
- [ ] 箭头 marker 的 fill 与线 stroke 同色
- [ ] 文字有 text-anchor，未靠 x 硬凑居中
- [ ] 节点未贴画布边(留白 ≥ 40px)
- [ ] 连线未被节点遮挡(箭头可见)
