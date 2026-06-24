#!/usr/bin/env python3
"""Diagram Master — SVG to PPTX 导出（自包含，不依赖 ppt-master）。

把 svg_output/ 下的 SVG 转成 PPTX：每张 SVG 一页，多张自动合并为多页。
矢量原生嵌入（DrawingML），filter/marker/阴影全部保留。

底层引擎：scripts/svg_to_pptx/ 内嵌包（源自 ppt-master，已随技能分发）。
第三方依赖：仅 python-pptx（pip install python-pptx）。

用法：
    python svg2pptx.py <project_path>            # 默认 16:9，输出到 exports/
    python svg2pptx.py <project_path> -f a4      # 竖图用 A4
    python svg2pptx.py <project_path> -o out.pptx # 指定输出文件名
    python svg2pptx.py <project_path> --help     # 看全部参数（动画/转场/旁白等）

退出码：0 成功；非 0 失败（见 stderr）。
"""
from __future__ import annotations

import sys
from pathlib import Path

# 关键：把本脚本所在目录加入 sys.path，使内嵌的 svg_to_pptx 包可被导入。
# 这样无论从哪个 cwd 调用、是否安装到 site-packages，都能找到包。
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

try:
    from svg_to_pptx import main as _pkg_main
except ImportError as e:
    sys.stderr.write(
        f"[svg2pptx] 无法加载内嵌的 svg_to_pptx 包：{e}\n"
        f"  请确认 {_HERE / 'svg_to_pptx'} 目录完整存在。\n"
        f"  第三方依赖：pip install python-pptx\n"
    )
    sys.exit(2)


def main(argv: list[str] | None = None) -> int:
    """转发到内嵌包的 CLI。argv=None 时读 sys.argv[1:]。"""
    return _pkg_main(argv)


if __name__ == "__main__":
    sys.exit(main())
