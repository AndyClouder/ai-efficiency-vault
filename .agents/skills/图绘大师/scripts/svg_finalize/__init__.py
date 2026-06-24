"""svg_finalize — 内嵌的 SVG 自包含化工具子集。

仅包含 diagram-master 的 svg_to_pptx 实际需要的两个模块：
  - flatten_tspan: 把带位置属性的 <tspan> 拍平成独立 <text>
  - embed_icons:   展开 <use data-icon="..."> 图标占位符

源自 ppt-master 的 svg_finalize 包，已随 diagram-master 分发，
不依赖 ppt-master。两个模块均仅依赖 Python 标准库。
"""
