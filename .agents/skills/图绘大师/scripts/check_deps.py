#!/usr/bin/env python3
"""Diagram Master — 依赖自检工具。

一键探测 diagram-master 各功能模块的依赖状态，输出"✓已装 / ✗未装(装什么)"
报告。帮助首次安装时快速定位缺哪些库。

用法：
    python check_deps.py            # 完整自检(Python 库 + 外部命令)
    python check_deps.py --py-only  # 只查 Python 库(跳过 pandoc)
    python check_deps.py --quiet    # 仅返回退出码：0 全装好，1 有缺失

退出码：0 = 全部就绪；1 = 有缺失（具体见输出）。
"""
from __future__ import annotations

import argparse
import importlib
import shutil
import sys
from importlib import util as importlib_util

# ─────────────────────────────────────────────────────────────
# 依赖清单：功能模块 → (展示名, pip 安装名, import 模块名)
# import 模块名用于探测；pip 安装名给用户复制命令（与 import 名不同时单独列出）
# ─────────────────────────────────────────────────────────────

# (展示名, pip_install_name, import_name)
DEPS = {
    # ── 核心：PPTX 导出 ──
    "PPTX 导出 (svg2pptx)": [
        ("python-pptx", "python-pptx", "pptx"),
    ],
    # ── 源转换：Word ──
    "源转换·Word (.docx)": [
        ("mammoth", "mammoth", "mammoth"),
        ("Pillow", "Pillow", "PIL"),
    ],
    # ── 源转换：Excel ──
    "源转换·Excel (.xlsx)": [
        ("openpyxl", "openpyxl", "openpyxl"),
    ],
    # ── 源转换：PDF ──
    "源转换·PDF": [
        ("PyMuPDF", "PyMuPDF", "fitz"),
    ],
    # ── 源转换：PowerPoint ──
    "源转换·PowerPoint (.pptx)": [
        ("python-pptx", "python-pptx", "pptx"),
        ("Pillow", "Pillow", "PIL"),
    ],
    # ── 源转换：网页 ──
    "源转换·网页": [
        ("requests", "requests", "requests"),
        ("beautifulsoup4", "beautifulsoup4", "bs4"),
        ("markdownify", "markdownify", "markdownify"),
        ("Pillow", "Pillow", "PIL"),
        ("curl_cffi", "curl_cffi", "curl_cffi"),
    ],
    # ── 源转换：HTML/EPUB/IPYNB (doc_to_md 的其他分支) ──
    "源转换·HTML/EPUB/IPYNB": [
        ("markdownify", "markdownify", "markdownify"),
        ("beautifulsoup4", "beautifulsoup4", "bs4"),
        ("requests", "requests", "requests"),
        ("ebooklib", "ebooklib", "ebooklib"),
        ("nbformat", "nbformat", "nbformat"),
        ("nbconvert", "nbconvert", "nbconvert"),
        ("Pillow", "Pillow", "PIL"),
    ],
}

# 外部命令（非 pip，需系统安装）
EXTERNAL_CMDS = {
    "pandoc": "转老式 .doc/.odt/.rtf（建议用户另存为 .docx 规避）",
}


def _probe_module(import_name: str) -> bool:
    """探测某 Python 模块能否 import。"""
    try:
        return importlib_util.find_spec(import_name) is not None
    except (ImportError, ValueError):
        # 某些包在 find_spec 阶段也会抛异常，退一步真 import
        try:
            importlib.import_module(import_name)
            return True
        except ImportError:
            return False


def _probe_command(cmd: str) -> bool:
    """探测某系统命令是否在 PATH。"""
    return shutil.which(cmd) is not None


def _version_of(import_name: str) -> str:
    """尝试取已装库的版本号，取不到就空串。"""
    try:
        mod = importlib.import_module(import_name)
        for attr in ("__version__", "version", "Version", "VERSION"):
            v = getattr(mod, attr, None)
            if isinstance(v, str):
                return v
        # fitz 特例
        if import_name == "fitz":
            return getattr(mod, "__doc__", "").split()[1] if mod.__doc__ else ""
    except Exception:
        pass
    return ""


def run_check(py_only: bool = False) -> int:
    """执行自检，返回缺失项数。打印报告。"""
    all_missing_pip: set[str] = set()
    missing_external: list[str] = []

    # Python 库探测
    print("=" * 62)
    print(" diagram-master 依赖自检")
    print("=" * 62)

    for module_name, deps in DEPS.items():
        print(f"\n【{module_name}】")
        module_missing: list[str] = []
        for display, pip_name, import_name in deps:
            if _probe_module(import_name):
                ver = _version_of(import_name)
                ver_str = f"  v{ver}" if ver else ""
                print(f"    ✓ {display}{ver_str}")
            else:
                print(f"    ✗ {display}  ← pip install {pip_name}")
                module_missing.append(pip_name)
                all_missing_pip.add(pip_name)

        if module_missing:
            print(f"    → 该功能当前不可用。装齐：pip install {' '.join(module_missing)}")
        else:
            print(f"    → 就绪 ✓")

    # 外部命令探测
    if not py_only:
        print(f"\n【外部命令（系统级，非 pip）】")
        for cmd, desc in EXTERNAL_CMDS.items():
            if _probe_command(cmd):
                print(f"    ✓ {cmd}")
            else:
                print(f"    ✗ {cmd}  ← 未安装（{desc}）")
                missing_external.append(cmd)
        if not missing_external:
            print(f"    → 就绪 ✓")

    # 汇总
    print("\n" + "=" * 62)
    if not all_missing_pip and not missing_external:
        print(" ✅ 全部就绪！所有功能可用。")
        return 0

    if all_missing_pip:
        print(f" ⚠️  缺 {len(all_missing_pip)} 个 Python 库：")
        print(f"    一键装全：pip install {' '.join(sorted(all_missing_pip))}")
    if missing_external:
        print(f" ⚠️  缺 {len(missing_external)} 个外部命令：{', '.join(missing_external)}")
        print("    （非必需，仅影响个别老格式；可忽略）")
    print("=" * 62)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="diagram-master 依赖自检：探测各功能模块缺哪些库。",
    )
    parser.add_argument(
        "--py-only", action="store_true",
        help="只查 Python 库，跳过 pandoc 等外部命令。",
    )
    parser.add_argument(
        "--quiet", "-q", action="store_true",
        help="静默模式：不打印报告，仅用退出码表示(0=就绪,1=有缺失)。",
    )
    args = parser.parse_args(argv)

    if args.quiet:
        # 静默：静默探测，有缺失就返回1
        for _, deps in DEPS.items():
            for _disp, _pip, imp in deps:
                if not _probe_module(imp):
                    return 1
        if not args.py_only:
            for cmd in EXTERNAL_CMDS:
                if not _probe_command(cmd):
                    # 外部命令缺失不算硬失败，quiet 模式仍返回0
                    pass
        return 0

    return run_check(py_only=args.py_only)


if __name__ == "__main__":
    sys.exit(main())
