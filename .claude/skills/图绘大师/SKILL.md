---
name: 图绘大师
description: >
  文章/文档/网页 → 结构化图、架构图、系统图的高保真 SVG 手绘助手。通过多角色协作
  (内容解析师 → 图表设计师 → 执行者) 把任意文字材料提炼成实体、关系、层级，并逐张
  手绘出可精确控制布局与配色的 SVG 图(分层架构/流程/时序/思维导图/框架/组件/数据流/
  层级/矩阵/循环/时间线/对比 共 12 类)。Use whenever the user says "画架构图"、"画系统图"、
  "画流程图"、"画时序图"、"把这段文章/文档/文字画成图"、"把文档转成图"、"diagram"、
  "架构图"、"流程图"、"系统图"、"思维导图"、"关系图"、"组件图"、"数据流图"，或
  mentions "图绘大师"。
---

# Diagram Master Skill

> 文章 → 结构化图 / 架构图 / 系统图的高保真 SVG 手绘助手。聚焦"单图或少量图"的精确手绘，**自带引擎**最终导出为可双击打开的 PPTX（每图一页，矢量无损）。完全自包含，不依赖其他 skill。不做带正文讲稿的整套 PPT

**核心流水线**：`源内容 → [转换] → [建项目] → [内容解析] → [⛔确认] → [SVG手绘] → [PPTX导出]`

> 最终交付物是 **PPTX**（单图单页 / 多图多页）。SVG 是中间产物，不作为主交付——很多环境 SVG 双击打不开或预览异常。

> [!CAUTION]
> ## 🚨 全局执行纪律(强制)
>
> 1. **串行执行** — 阶段按序进行，前一步输出是后一步输入。非 ⛔ 阻塞步骤在前提满足后可连续推进，无需等用户说"继续"。
> 2. **⛔ BLOCKING = 硬停** — Step 4 的确认是唯一阻塞点，必须等用户明确回复后才推进。确认后，Step 5 手绘与 Step 6 导出可自动连续完成。
> 3. **GATE 前先验证** — 每个阶段顶部的 🚧 GATE 前提必须先核验再进入。
> 4. **SVG 必须手写，禁止脚本生成** — 每张 SVG 由当前主代理逐张手写，禁止用 Python/Node/Shell 脚本批量产出。跨页视觉一致性依赖逐图创作 + 上游上下文。
> 5. **逐图重读 spec_lock** — 画每张图前必须 `read_file <project_path>/spec_lock.md`，颜色/字体/图标只取自此文件，不用记忆值。
> 6. **禁止投机执行** — 不准"提前准备"后续阶段产物(如 Step 3 就开始写 SVG)。

> [!IMPORTANT]
> ## 🌐 语言规则
> - **回答语言**：匹配用户输入与源材料。用户显式覆盖优先(如"请用英文回答")。
> - **图内文字语言**：跟随源材料语言。源是中文则图内用中文；用户明确要求双语时才双语。

> [!IMPORTANT]
> ## 🧩 自包含说明(必读)
>
> 本技能**完全独立**，源文件转换 + PPTX 导出的引擎都已内嵌，**不依赖 ppt-master 或任何其他 skill**。开箱即用。
>
> | 能力 | 来源 | 第三方依赖(pip) |
> |---|---|---|
> | **源文件转 Markdown** | 本技能自带 `scripts/source_to_md/`(5 脚本，覆盖 Word/Excel/PDF/PPT/网页/EPUB/IPYNB) | 按格式定，见 Step 1 |
> | **PPTX 导出** | 本技能自带 `scripts/svg2pptx.py` + 内嵌 `scripts/svg_to_pptx/` 包 + `scripts/svg_finalize/` | `python-pptx` |
> | SVG 手绘模板 | 本技能自带 `templates/charts/`(15 个) | 无 |
> | 项目管理 | 本技能自带 `scripts/project_manager.py` | 无 |
>
> **导出引擎说明**：`scripts/svg_to_pptx/` 是 SVG→DrawingML 矢量转换包(源自 ppt-master，已随本技能完整内嵌分发)，把 SVG 原生矢量嵌入 PPTX，filter/marker/阴影全保留，放大无损。
>
> **源转换说明**：`scripts/source_to_md/` 是 5 个独立转换器(源自 ppt-master，已内嵌)。各格式**按需** `import` 对应第三方库——只装你用的格式的库即可，未装的格式会提示缺哪个库，不影响其他格式。
>
> **职责边界**：本技能做"源文件→结构化图→PPTX"全链路。若用户要"带正文讲稿的整套演示文稿"，引导其走 ppt-master。

> **Windows 提示**：`python3` 命令在部分 Windows 安装上会失败(只有 `python.exe`)，此时改用 `python` 重试同一命令。

---

## 主流水线脚本

| 脚本 | 用途 | 依赖 |
|---|---|---|
| `${SKILL_DIR}/scripts/project_manager.py` | 项目初始化 / 导入源文件 / 校验 | 无(自带) |
| `${SKILL_DIR}/scripts/source_to_md/*.py` | **源文件 → Markdown**(Word/Excel/PDF/PPT/网页等，自带) | 按格式，见 Step 1 |
| `${SKILL_DIR}/scripts/svg2pptx.py` | **SVG → PPTX 导出**(核心交付，每图一页) | `python-pptx`(自带引擎) |
| `${SKILL_DIR}/scripts/check_deps.py` | **依赖自检**(探测缺哪些库，给装库命令) | 无(纯标准库) |

## 模板索引

| 索引 | 路径 | 用途 |
|---|---|---|
| 图类型库 | `${SKILL_DIR}/references/diagram-types/_index.md` | 12 种图类型目录 + 自动选择表 |
| SVG 模板 | `${SKILL_DIR}/templates/charts/` | 15 个手绘参考模板(layered_architecture / client_server_flow / process_flow 等)，详见目录下 README.md |

---

## Workflow

### Step 1: 源内容转换

🚧 **GATE**：用户已提供源材料(PDF / DOCX / EPUB / URL / Markdown / 纯文本 / 对话内容 — 任意形式皆可)。

当用户提供的不是 Markdown/纯文本时，用本技能**自带的**转换脚本(`${SKILL_DIR}/scripts/source_to_md/`)转成 Markdown。**完全自包含，不依赖 ppt-master。**

> 💡 **首选输入仍是 Markdown / 纯文本 / 对话描述**——解析(Step 3)直接消费文本。转换脚本只在用户给的是二进制文件时才用。

#### 转换命令(Windows 用 `python`，Linux/Mac 用 `python3`)

| 用户提供 | 命令 | 需 pip 安装的库(按需) |
|---|---|---|
| **DOCX / Word** | `python ${SKILL_DIR}/scripts/source_to_md/doc_to_md.py <file>` | `mammoth Pillow` |
| HTML / EPUB / IPYNB | `python ${SKILL_DIR}/scripts/source_to_md/doc_to_md.py <file>` | `markdownify beautifulsoup4 requests ebooklib nbformat nbconvert Pillow` |
| **XLSX / Excel** | `python ${SKILL_DIR}/scripts/source_to_md/excel_to_md.py <file>` | `openpyxl` |
| **PDF** | `python ${SKILL_DIR}/scripts/source_to_md/pdf_to_md.py <file>` | `PyMuPDF` |
| **PPTX / PowerPoint** | `python ${SKILL_DIR}/scripts/source_to_md/ppt_to_md.py <file>` | `python-pptx Pillow` |
| **网页链接**(含微信公众号) | `python ${SKILL_DIR}/scripts/source_to_md/web_to_md.py <URL>` | `requests beautifulsoup4 markdownify Pillow curl_cffi` |
| Markdown / 纯文本 / 对话内容 | 直接读取，无需转换 | 无 |

> 一键装全(支持全部格式)：`pip install mammoth Pillow requests beautifulsoup4 markdownify ebooklib nbformat nbconvert openpyxl PyMuPDF python-pptx curl_cffi`

#### 报错处理
- `ModuleNotFoundError: No module named 'xxx'` → 该格式的库没装。按上表 `pip install` 对应库后重试。脚本按需 import，**只装你用的格式的库即可**。
- 老 `.doc/.odt/.rtf` → 需系统装 `pandoc`(外部命令，非 pip)。建议让用户另存为 `.docx`。
- 转换失败 → 退路：让用户把内容(或关键段落)直接以 Markdown/纯文本贴进对话。

**✅ Checkpoint — 源内容已就绪，进入 Step 2。**

---

### Step 2: 项目初始化

🚧 **GATE**：Step 1 完成；源内容可读(Markdown 文件 / 用户文本 / 对话描述皆可)。

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py init <project_name>
```

项目结构(`projects/<name>/`)：
```
sources/        # 源文件(转换后的 MD + 原始文件)
svg_output/     # 手绘 SVG 输出
analysis.md     # Step 3 产出的结构化解析
spec_lock.md    # Step 4 确认后的视觉规格锁
```

导入源文件(有文件时)：
```bash
python3 ${SKILL_DIR}/scripts/project_manager.py import-sources <project_path> <source_files...> --move
```

> ⚠️ **务必用 `--move`**：所有源文件(Step 1 的 MD + 原始 PDF/MD/图片)经 `import-sources --move` 进入 `sources/`，执行后原位置不再保留。
> 若用户是在对话里直接给文本，则无需导入，后续步骤直接引用对话内容。

**✅ Checkpoint — 项目结构创建成功，`sources/` 含全部源文件。进入 Step 3。**

---

### Step 3: 内容解析师阶段(角色 1，不可跳过)

🚧 **GATE**：Step 2 完成；项目目录就绪。

先读角色定义：
```
Read references/analyzer.md
```

**任务**：通读源内容，提炼出可被"图"承载的结构。输出写入 `<project_path>/analysis.md`，必含以下五块：

| 块 | 内容 | 示例 |
|---|---|---|
| **实体清单** | 名词/组件/角色/系统(去重、规范化命名) | `API网关` / `用户服务` / `Redis` |
| **关系清单** | 实体间的连接(带方向与类型) | `用户服务 → 调用 → Redis` |
| **层级结构** | 树/分层/并列的组织关系 | `应用层 { Web, App }` |
| **关键数据** | 数字/时间/对比项(若存在) | `QPS 10万` / `2024-2026` |
| **推荐图类型** | 从 12 种里选 1-3 个，每个附 1 句理由 | `分层架构(明显的三层栈)` |

> 参考图类型目录：`references/diagram-types/_index.md` 的自动选择表。

> ⚠️ **不要在解析阶段开始画图或写 SVG**。本阶段只产出结构化文字。

**✅ Checkpoint — `analysis.md` 写完，五块齐全。进入 Step 4。**

---

### Step 4: 确认阶段(⛔ BLOCKING — 唯一硬停点)

🚧 **GATE**：Step 3 完成；`analysis.md` 已生成。

⛔ **BLOCKING**：把以下三项作为一个推荐集合一次性呈现，**等用户明确确认或修改后**才能继续。这是核心确认点 — 一旦确认，Step 5 手绘与 Step 6 导出自动连续完成，无需二次确认。

**三项确认**：

1. **图类型与张数** — 基于解析结果推荐 1-3 张图，每张一个类型(见 `diagram-types/_index.md`)。例如：
   - 图1：分层架构图(系统全貌)
   - 图2：时序图(关键请求链路)
2. **要素清单** — 每张图要画的实体/关系/层级，逐图列出，请用户核对有无遗漏或冗余。
3. **视觉规格** — 一次性给出推荐默认值，用户可改：
   - 画布：`1280×720`(默认 16:9)
   - 配色：`#1E3A5F`(主色 深海军蓝) / `#F8F9FA`(底 浅灰) / `#D4AF37`(强调 金) / `#0F172A`(正文)
   - 字体：`-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif`
   - 语言：跟随源材料
   - 图标：是否使用字母占位图标(默认是)

确认后，把这些规格写入 `<project_path>/spec_lock.md`(机器可读契约，执行者每张图前重读)。

> 若用户只回"可以"/"继续"/"OK"即视为全部采纳推荐；若改某项(如"配色换成绿色")，其余项保持推荐默认。

**✅ Checkpoint — Phase 交付完成，自动推进到 Step 5**：
```markdown
## ✅ 确认阶段完成
- [x] 三项确认已完成(用户在聊天中确认)
- [x] spec_lock.md 已生成
- [ ] **下一步**：自动进入执行者阶段，逐张手绘 SVG
```

---

### Step 5: 执行者阶段(角色 3，手绘 SVG)

🚧 **GATE**：Step 4 完成；`spec_lock.md` 已生成且用户已确认。

先按本批图的类型读执行参考：
```
Read references/executor-base.md          # 必读：通用手绘规范
Read references/shared-standards.md       # 必读：SVG 技术约束(禁用特性/坐标系/文本)
Read references/diagram-types/<type>.md   # 每种用到的图类型各读一次
```

> 按需参考已硬拷贝的模板：`Read templates/charts/<相关模板>.svg`(例如画分层架构读 `layered_architecture.svg`)。模板提供结构骨架与配色逻辑，但颜色/字体必须重绘为 `spec_lock.md` 的值。

**设计参数确认(强制)**：第一张图前，输出关键设计参数(画布尺寸、配色 HEX、字体、正文字号)，防止规格与执行漂移。

**逐图重读 spec_lock(强制)**：每张图前 `read_file <project_path>/spec_lock.md`，只用其中的颜色/字体/图标，不用记忆值。抵抗长上下文压缩导致的漂移。

> ⚠️ **主代理专用**：SVG 手绘必须留在当前主代理，图设计依赖完整上游上下文。禁止委托子代理。
> ⚠️ **逐张手绘**：在同一个连续上下文里一张接一张画，不要批处理(如"一次画 3 张")。

**视觉构建阶段**：逐张手绘 SVG → `<project_path>/svg_output/`，命名 `<NN>_<type>.svg`(如 `01_architecture.svg` / `02_sequence.svg`)。

**自检门(强制)** — 每张图画完后逐项核对(无需脚本)：
- [ ] 实体/关系/层级是否与 `analysis.md` 一致(无遗漏无多余)
- [ ] 连线方向是否正确(箭头指向)
- [ ] 无禁用 SVG 特性(见 `shared-standards.md`：mask / `<style>` / `<foreignObject>` / `<script>` / 动画 / `textPath`)
- [ ] viewBox 与画布尺寸一致
- [ ] 所有颜色/字体来自 `spec_lock.md`
- [ ] XML 合法(`&` → `&amp;`，`<` → `&lt;`；typography 符号用原始 Unicode，不用 HTML 实体)

**✅ Checkpoint — 全部 SVG 手绘完成且自检通过**：
```markdown
## ✅ 执行者阶段完成
- [x] 所有 SVG 已手绘到 svg_output/
- [x] 逐图自检通过(要素齐全 / 连线正确 / 无禁用特性 / viewBox 匹配)
```

---

### Step 6: 后处理与导出

🚧 **GATE**：Step 5 完成；`svg_output/` 内 SVG 齐全且自检通过。

> [!IMPORTANT]
> ## 🎯 默认交付物 = PPTX
> 从 Step 5 自检通过后**自动执行** PPTX 导出，无需用户再开口。SVG 是中间产物，**不要把"浏览器预览 SVG"作为主交付**——很多环境下 SVG 双击打不开 / 预览器渲染异常。最终给用户一个能直接打开的 `.pptx`。

#### 6.1 导出 PPTX（默认，强制执行）

每张 SVG 入一页，多张图自动合并为多页 PPTX。**本技能自包含导出引擎**（`${SKILL_DIR}/scripts/svg2pptx.py` + 内嵌的 `svg_to_pptx/` 包），不依赖任何外部 skill。命令（Windows 用 `python`，Linux/Mac 用 `python3`）：

```bash
# Windows
python ${SKILL_DIR}/scripts/svg2pptx.py <project_path> -f ppt169 -q
# Linux / macOS
python3 ${SKILL_DIR}/scripts/svg2pptx.py <project_path> -f ppt169 -q
```

- 输出位置：**`<vault根>/ppt_outputs/<时间戳>.pptx`**（脚本自动检测 vault 根——以含 `0_系统配置/` 或 `.agents/` 为标志——并在其下建 `ppt_outputs/` 目录；不在 vault 内时回退到 `<project_path>/exports/`）。
- `-f ppt169` = 16:9 画布（与 1280×720 / 1280×860 等横向画布匹配）。竖图(如纵向流程)改 `-f a4`。
- 多图多页：把多张 SVG 放进 `svg_output/`，脚本按文件名排序，每张一页。
- **画布自适应**：若 spec_lock 画布非 16:9（如 1280×860 ≈ 3:2），优先选最接近的 `-f`；差太大时在脚本前提醒用户，或仍用 `ppt169` 由脚本按比例铺满。

> **唯一第三方依赖**：`python-pptx`。首次使用前确认已装：`pip install python-pptx`。
>
> 若脚本报错：
> - 报 `No module named 'pptx'` → `pip install python-pptx` 后重试。
> - 报找不到 SVG → 确认 `svg_output/*.svg` 存在；脚本默认读 `svg_output/`（native 模式，高保真矢量 DrawingML）。
> - 仍失败 → 退路：用 `--only legacy` 走 PPT 内置 SVG 解析，或改导出 PNG（见 6.3）。

#### 6.2 本地预览（仅当用户明确要"看 SVG 源"）

> ⚠️ 非默认。仅在用户问"SVG 长什么样"或要调试 SVG 时给出。**不作为交付项。**

```bash
# 推荐用 VS Code / 浏览器拖入 svg_output/ 下的文件直接看。
# 命令行起静态服务器(注意：老版 Python 不支持 -d 参数)：
cd <project_path>/svg_output && python -m http.server 8000
# 浏览器打开 http://localhost:8000/<NN>_<type>.svg
```

#### 6.3 导出 PNG（备选，当 PPTX 不可用或用户要图片）

```bash
# Inkscape
inkscape <project_path>/svg_output/01_architecture.svg --export-type=png --export-width=2560
# 无 Inkscape 时：用浏览器打开 SVG → 右键"另存为图片"，或截图。
```

**✅ Checkpoint — 导出完成**（必须给出文件路径，让用户能找到）：
```markdown
## ✅ 全流程完成
- [x] 源内容转换 / 项目初始化 / 内容解析 / 确认 / SVG 手绘 / PPTX 导出 全部完成
- [x] 产物：
  - SVG 源：<project_path>/svg_output/*.svg
  - **PPTX（交付）：<vault根>/ppt_outputs/<文件名>.pptx**  ← 双击打开
```

---

## 角色切换协议

切换角色前，**必须先读**对应参考文件。输出标记：
```markdown
## [角色切换: <角色名>]
📖 读取角色定义: references/<filename>.md
📋 当前任务: <简述>
```

角色清单：
| 角色 | 参考文件 | 阶段 |
|---|---|---|
| 内容解析师 | `references/analyzer.md` | Step 3 |
| 图表设计师 | `references/designer.md` | Step 3-4(选图类型时的辅助) |
| 执行者 | `references/executor-base.md` | Step 5 |

---

## 参考资源

| 资源 | 路径 |
|---|---|
| SVG 技术约束(禁用特性/坐标系/文本规则) | `references/shared-standards.md` |
| 图类型库(12 种 + 自动选择表) | `references/diagram-types/_index.md` |
| SVG 模板(15 个) | `templates/charts/` (见 README.md) |
| 常见问题 | `docs/faq.md` |

---

## 备注

- **默认交付 PPTX**：`python ${SKILL_DIR}/scripts/svg2pptx.py <project_path> -f ppt169 -q`，产物在 **`<vault根>/ppt_outputs/`**（vault 外回退 `<project_path>/exports/`）。默认 native 模式（可编辑的 DrawingML 形状），引擎自包含，仅依赖 `pip install python-pptx`。
- **SVG 预览仅用于调试**：用 VS Code / 浏览器拖入 `svg_output/*.svg`；不作为交付物（多数环境 SVG 双击打不开）。
- **故障排查**：生成问题(布局溢出 / SVG 不显示 / 箭头丢失)查 `docs/faq.md`；导出失败见 Step 6 的退路说明。
- **职责边界**：本技能做"单图或少量高保真手绘"。若用户要整套带文字的演示文稿，引导其走 ppt-master；若用户只要快速草图，建议直接用 Mermaid(本技能不在其列)。

---

## 🔧 安装与可移植性

本技能**完全自包含**，可整体复制到任何机器人/agent 框架使用。

### 路径约定
- 文中 `${SKILL_DIR}` = 本技能根目录（含 SKILL.md 的目录）。agent 框架应将其替换为实际安装路径。
- 所有脚本/模板/参考都用相对 `${SKILL_DIR}` 的路径，**无硬编码绝对路径、无环境变量依赖**。

### 安装前置

```bash
# 最小依赖（仅 PPTX 导出）
pip install python-pptx
```

源文件转 Markdown(Word/Excel/PDF 等) 按格式按需装库，见 Step 1 表格。
**一键装全**：`pip install mammoth Pillow requests beautifulsoup4 markdownify ebooklib nbformat nbconvert openpyxl PyMuPDF python-pptx curl_cffi`

> 无需 cairosvg / svglib / Inkscape / LibreOffice / cairo 系统库。
> 无需安装 ppt-master 或任何其他 skill。

### 目录结构（复制时需完整保留）
```
图绘大师/
├── SKILL.md
├── scripts/
│   ├── project_manager.py        # 项目管理(纯标准库)
│   ├── check_deps.py             # 依赖自检(纯标准库)
│   ├── svg2pptx.py               # PPT 导出入口(自包含)
│   ├── source_to_md/             # 源文件转 Markdown(5 转换器)
│   ├── svg_to_pptx/              # 内嵌矢量转换引擎(19 文件)
│   └── svg_finalize/             # 内嵌 SVG 预处理(2 模块)
├── templates/charts/             # 15 个 SVG 手绘模板
└── references/                   # 图类型规范 + 角色定义
```

### 验证安装（先跑自检，再跑功能测试）

**① 依赖自检**（推荐第一步，秒级，告诉你缺什么）：
```bash
python <skill_dir>/scripts/check_deps.py
```
输出示例（缺库时会直接给 `pip install` 命令）：
```
【源转换·Word (.docx)】
    ✗ mammoth  ← pip install mammoth
    → 该功能当前不可用。装齐：pip install mammoth Pillow
...
⚠️ 缺 3 个 Python 库：
    一键装全：pip install Pillow mammoth openpyxl
```

**② 功能测试**（自检通过后，实际跑一次）：
```bash
# PPTX 导出: 任意 SVG → PPTX
python <skill_dir>/scripts/svg2pptx.py <any_project_with_svg_output> -f ppt169 -q
# 看到 "Converted N elements" + "Saved: exports/xxx.pptx" 即成功

# 源转换(以 Word 为例):
python <skill_dir>/scripts/source_to_md/doc_to_md.py <任意.docx>
```

### 可选(非必需)
- **pptx_animations**：若装了此包可启用 PPT 动画/转场；不装也能正常导出（仅无动画效果）。
- **pandoc**(系统命令)：转老式 `.doc/.odt/.rtf`；不装就让用户另存为 `.docx`。

