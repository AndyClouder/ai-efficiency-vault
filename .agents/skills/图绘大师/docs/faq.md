# 常见问题(FAQ)

> 生成与导出过程中的典型问题与解决方案。

---

## Q1：源文件转换失败(PDF/DOCX/网页转不出 Markdown)

**原因**：本技能复用 ppt-master 的 `source_to_md/*` 脚本，若 ppt-master 未安装、被移动，或脚本依赖缺失(`curl_cffi`、`pandoc` 等)，转换会失败。

**排查**：
1. 确认 ppt-master 在 `C:\Users\114643\.agents\skills\ppt-master`(或 SKILL.md 顶部 `PPT_MASTER_DIR` 指向的位置)。
2. 单独跑转换脚本看报错：
   ```bash
   python C:/Users/114643/.agents/skills/ppt-master/scripts/source_to_md/pdf_to_md.py <你的文件>
   ```
3. 网页转换失败 → 多半是反爬，试试 `curl_cffi` 模式(微信文章必装)。
4. 若 ppt-master 确实不在 → 让用户手动把内容转成 Markdown/纯文本贴进对话，跳过转换直接进 Step 2。

---

## Q2：`python3` 命令不存在(Windows)

**原因**：python.org 的 Windows 安装只提供 `python.exe`，没有 `python3.exe`。

**解决**：把 SKILL.md / 文档里的 `python3` 改用 `python` 重试同一命令即可。

---

## Q3：SVG 在浏览器里不显示 / 显示空白

**排查清单**：
- **XML 非法**：检查有没有裸 `&` `<` `>`(必须转义为 `&amp;` `&lt;` `&gt;`)；有没有用了 HTML 命名实体(`&mdash;` `&rarr;` —— 必须用原始 Unicode 字符 `—` `→`)。
- **viewBox 缺失**：`<svg>` 必须有 `viewBox="0 0 W H"` 且 W/H 与 `width`/`height` 一致。
- **禁用特性**：用了 `mask` / `<style>` / `<foreignObject>` / `<script>` 等(见 `references/shared-standards.md` §2)。
- **引用不存在的 id**：`filter="url(#cardShadow)"` 但 `<defs>` 里没定义 `cardShadow`。

**快速验证**：用浏览器直接打开 SVG 文件，按 F12 看 Console 报错。

---

## Q4：箭头丢失 / 不显示

**原因**：`<marker>` 不满足条件(见 `shared-standards.md` §2.1)。

**检查**：
- `<marker>` 是否在 `<defs>` 内
- `orient="auto"`(否则不沿线旋转)
- marker 的 `fill` 是否与线条 `stroke` **同色**
- 形状是否是三角/菱形/圆(其他形状会被丢)

**临时绕过**：用独立的 `<polygon>` 画箭头头部，不依赖 marker。

---

## Q5：文字溢出节点 / 排版错乱

**原因**：SVG 的 `<text>` 不自动换行。

**解决**：
- 长文本拆成多个 `<text>`(每行一个)或一个 `<text>` + 多个 `<tspan dy="...">`
- 节点标题 ≤ 8 中文字；说明每行 ≤ 16 中文字
- 居中用 `text-anchor="middle"`，别靠 x 坐标硬凑
- 行距 = 字号 × 1.4(中文)

---

## Q6：导出 PNG 模糊

**原因**：截图分辨率低。

**解决**：
- Inkscape 指定高分辨率：`inkscape in.svg --export-type=png --export-width=2560`(2× 画布宽)
- 或浏览器缩放到 200% 再截图
- 或用 `svgexport`(Node 工具)：`svgexport in.svg out.png 2x`

---

## Q7：导出 PPTX 失败

**原因**：软引用 ppt-master 的 `svg_to_pptx.py`，路径或依赖问题。

**解决**：
1. 确认 ppt-master 已安装且 `svg_to_pptx.py` 可跑。
2. 单图场景通常直接：
   ```bash
   python C:/Users/114643/.agents/skills/ppt-master/scripts/svg_to_pptx.py <project_path>
   ```
3. 若失败且不需要可编辑 PPT，**推荐改走 PNG 截图插入 PPT**(更简单可靠)。

---

## Q8：图类型选错了，画出来不对

**判断标准**(见 `references/diagram-types/_index.md` §2 自动选择表)：
- 有先后顺序 → flowchart / sequence / data-flow / timeline
- 有分层结构 → architecture / hierarchy
- 围绕中心 → framework / mindmap
- 闭环 → cycle
- 对比 → comparison / matrix

**改图类型**：在 Step 4 确认时改；若已画完才发现，回到 Step 3 重新解析 + Step 4 重新确认 + Step 5 重画。

---

## Q9：一张图要表达的信息太多，挤不下

**原则**：一张图一个主结构。信息多就**拆成多张图**：
- 系统全貌(architecture) + 关键链路(sequence)
- 整体流程(flowchart) + 数据视角(data-flow)
- 现状(comparison-前) + 目标(comparison-后)

超过 3 张时，提醒用户考虑是否合并或只画最关键的。

---

## Q10：用户只要一张快速草图，不需要高保真

**建议**：本技能是重量级手绘流程，适合 1-5 张高质量图。若用户只要快速草图，建议直接用 Mermaid：
```
告诉用户：你这个场景用 Mermaid 更快：
  flowchart LR
    A --> B --> C
本技能适合需要精确控制布局与配色的高保真图。
```
