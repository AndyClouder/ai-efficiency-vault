# 图绘大师 安装指南

> 结构化图 / 架构图 / 系统图的高保真 SVG 手绘助手，自带引擎导出可双击打开的 PPTX。
> **完全自包含**，不依赖 ppt-master 或任何其他 skill。

## 1. 前置依赖（唯一）

```bash
# 最小依赖(仅 PPTX 导出)
pip install python-pptx
```

### 源文件转 Markdown(按需，按格式装)

技能自带转换脚本，支持 Word/Excel/PDF/PPT/网页/EPUB/IPYNB 等。**按你用的格式安装对应库**，不装的格式不影响其他功能：

```bash
# 一键装全(支持所有格式)
pip install mammoth Pillow requests beautifulsoup4 markdownify ebooklib nbformat nbconvert openpyxl PyMuPDF python-pptx curl_cffi
```

| 格式 | 需装的库 |
|---|---|
| Word(.docx) | `mammoth Pillow` |
| Excel(.xlsx) | `openpyxl` |
| PDF | `PyMuPDF` |
| PowerPoint(.pptx) | `python-pptx Pillow` |
| 网页/微信公众号 | `requests beautifulsoup4 markdownify Pillow curl_cffi` |
| HTML / EPUB / IPYNB | `markdownify beautifulsoup4 requests ebooklib nbformat nbconvert Pillow` |
| 老 .doc/.odt/.rtf | 需系统装 `pandoc`(外部命令) |

不需要：cairosvg / svglib / Inkscape / LibreOffice / cairo 系统库 / ppt-master 或任何其他 skill。

## 2. 安装

把压缩包解压到你的 agent skills 目录：

```
<skills 目录>/图绘大师/
├── SKILL.md
├── INSTALL.md          ← 本文件
├── scripts/
│   ├── project_manager.py
│   ├── svg2pptx.py        ← PPT 导出入口
│   ├── source_to_md/      ← 源文件转 Markdown（5 个转换器）
│   ├── svg_to_pptx/       ← 内嵌矢量转换引擎（必须完整保留）
│   └── svg_finalize/      ← 内嵌 SVG 预处理（必须完整保留）
├── templates/charts/      ← 15 个 SVG 手绘模板
├── references/            ← 图类型规范 + 角色定义
└── docs/                  ← FAQ
```

> ⚠️ `scripts/svg_to_pptx/` 和 `scripts/svg_finalize/` 两个子目录**必须连同 `__init__.py` 完整保留**，漏任何一个文件都无法导出 PPTX。`scripts/source_to_md/` 5 个脚本也需完整保留才能转 Word 等格式。

## 3. 验证安装

### 第一步：依赖自检（推荐先跑，秒级出结果）
```bash
python <skills目录>/图绘大师/scripts/check_deps.py
```

这会逐个探测各功能模块（PPTX 导出 / Word / Excel / PDF / PPT / 网页 / EPUB 转换）缺哪些库，
缺库时直接给出 `pip install` 命令。全绿即所有功能就绪。

输出示例（缺库时）：
```
【源转换·Word (.docx)】
    ✗ mammoth  ← pip install mammoth
    → 该功能当前不可用。装齐：pip install mammoth Pillow
⚠️ 缺 3 个 Python 库：
    一键装全：pip install Pillow mammoth openpyxl
```

### 第二步：功能测试（自检通过后实跑）

**PPTX 导出**(任意带 SVG 的项目)：
```bash
python <skills目录>/图绘大师/scripts/svg2pptx.py <任意含 svg_output/ 的项目路径> -f ppt169 -q
```

**源文件转换**(以 Word 为例)：
```bash
python <skills目录>/图绘大师/scripts/source_to_md/doc_to_md.py <任意.docx文件>
```

看到下面输出即安装成功：
```
Converted N elements, skipped 0
[1/1] xxx.svg (Native)
[Done] Saved: exports/xxx.pptx
```

## 4. 路径约定

SKILL.md 文中所有 `${SKILL_DIR}` 指本技能根目录（含 SKILL.md 的目录）。
- ZCode / 大多数 agent 框架会自动替换该占位符
- 若你的框架不替换，请把命令里的 `${SKILL_DIR}` 手动改成实际安装路径

## 5. 用法速览

完整流程见 `SKILL.md`。最常用命令：

```bash
# 初始化项目
python <skill_dir>/scripts/project_manager.py init <项目名>

# （在项目里手绘 SVG 到 svg_output/ 后）导出 PPTX
python <skill_dir>/scripts/svg2pptx.py <项目路径> -f ppt169 -q
```

产物：`<项目路径>/exports/<时间戳>.pptx`，每张 SVG 一页，矢量无损。

## 6. 可选增强（非必需）

| 可选依赖 | 装了能怎样 | 不装的影响 |
|---|---|---|
| `pptx_animations` | 启用 PPT 动画/转场 | 仍能正常导出，只是无动画 |
| `ppt-master`（另一 skill） | 借用其脚本把 PDF/DOCX 转成 Markdown 输入 | 直接贴 Markdown/纯文本即可（本技能首选输入） |

## 7. 环境要求

- Python 3.9+
- Windows / macOS / Linux 均可
- 首次运行时 `python` / `python3` 命令二选一（Windows 通常只有 `python`）

