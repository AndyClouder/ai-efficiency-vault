#!/usr/bin/env python3
"""Diagram Master — 轻量项目管理脚本。

子命令：
    init <project_name>              创建项目目录骨架
    import-sources <project> <files...> [--move]   导入源文件到 sources/
    validate <project>               校验项目结构完整性
    info <project>                   打印项目元信息

项目结构(projects/<name>/)：
    sources/        源文件(转换后的 MD + 原始文件)
    svg_output/     手绘 SVG 输出
    analysis.md     Step 3 产出的结构化解析(由 AI 写入)
    spec_lock.md    Step 4 确认后的视觉规格锁(由 AI 写入)
    project.json    项目元信息

用法示例：
    python3 scripts/project_manager.py init my-diagram
    python3 scripts/project_manager.py import-sources projects/my-diagram report.md --move
    python3 scripts/project_manager.py validate projects/my-diagram
    python3 scripts/project_manager.py info projects/my-diagram
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

# 项目内固定子目录
SUBDIRS = ["sources", "svg_output"]
META_FILE = "project.json"
ANALYSIS_FILE = "analysis.md"
SPEC_LOCK_FILE = "spec_lock.md"


def _resolve_project_root(start: Path) -> Path:
    """从给定路径向上找含有 project.json 的目录；找不到则用 start 本身。"""
    start = start.resolve()
    if (start / META_FILE).exists():
        return start
    for parent in [start] + list(start.parents):
        if (parent / META_FILE).exists():
            return parent
    return start


def cmd_init(args):
    name = args.project_name
    if "/" in name or "\\" in name or name.startswith("."):
        print(f"错误：项目名不能含路径分隔符或以点开头: {name}", file=sys.stderr)
        return 1
    root = Path("projects") / name
    if root.exists():
        print(f"错误：项目已存在: {root}", file=sys.stderr)
        return 1
    for sub in SUBDIRS:
        (root / sub).mkdir(parents=True, exist_ok=True)
    # 占位文件(由 AI 在后续步骤填充)
    (root / ANALYSIS_FILE).write_text(
        f"# 内容解析：{name}\n\n> 由 Step 3 内容解析师阶段填充。\n",
        encoding="utf-8",
    )
    (root / SPEC_LOCK_FILE).write_text(
        f"# 视觉规格锁：{name}\n\n> 由 Step 4 确认阶段填充。\n",
        encoding="utf-8",
    )
    meta = {
        "name": name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "format": args.format,
        "stage": "initialized",  # initialized -> analyzed -> confirmed -> drawn -> exported
    }
    (root / META_FILE).write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"✅ 项目已创建: {root}")
    print(f"   画布格式: {args.format}")
    print(f"   下一步: 导入源文件或直接在对话中提供文本，进入 Step 3 解析")
    return 0


def cmd_import_sources(args):
    project = _resolve_project_root(Path(args.project_path))
    if not (project / META_FILE).exists():
        print(f"错误：不是有效项目目录(缺 {META_FILE}): {project}", file=sys.stderr)
        return 1
    sources_dir = project / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    moved = 0
    copied = 0
    missing = 0
    for f in args.files:
        src = Path(f)
        if not src.exists():
            print(f"⚠️  文件不存在，跳过: {f}", file=sys.stderr)
            missing += 1
            continue
        dst = sources_dir / src.name
        if args.move:
            shutil.move(str(src), str(dst))
            moved += 1
            print(f"📦 移动: {src} -> {dst}")
        else:
            shutil.copy2(str(src), str(dst))
            copied += 1
            print(f"📄 复制: {src} -> {dst}")
    print(f"完成: 移动 {moved} / 复制 {copied} / 缺失 {missing}")
    return 0 if missing == 0 else 2


def cmd_validate(args):
    project = _resolve_project_root(Path(args.project_path))
    errors = []
    warnings = []
    if not (project / META_FILE).exists():
        errors.append(f"缺少 {META_FILE} —— 不是有效项目目录")
        _print_result(project, errors, warnings)
        return 1
    for sub in SUBDIRS:
        if not (project / sub).is_dir():
            errors.append(f"缺少子目录: {sub}/")
    # analysis.md / spec_lock.md 在 init 时已建占位，这里只看是否仍是占位
    analysis = project / ANALYSIS_FILE
    if analysis.exists() and len(analysis.read_text(encoding="utf-8").strip()) < 40:
        warnings.append(f"{ANALYSIS_FILE} 仍是占位(Step 3 未执行)")
    spec = project / SPEC_LOCK_FILE
    if spec.exists() and len(spec.read_text(encoding="utf-8").strip()) < 40:
        warnings.append(f"{SPEC_LOCK_FILE} 仍是占位(Step 4 未执行)")
    svgs = list((project / "svg_output").glob("*.svg")) if (project / "svg_output").is_dir() else []
    if not svgs:
        warnings.append("svg_output/ 为空(Step 5 未执行)")
    else:
        # 基本校验：每个 SVG 有 viewBox 和 <svg
        for svg in svgs:
            txt = svg.read_text(encoding="utf-8", errors="replace")
            if "viewBox" not in txt:
                warnings.append(f"{svg.name} 缺 viewBox")
            if "<svg" not in txt:
                errors.append(f"{svg.name} 不是有效 SVG(无 <svg 标签)")
    _print_result(project, errors, warnings, svg_count=len(svgs))
    return 1 if errors else 0


def _print_result(project, errors, warnings, svg_count=0):
    print(f"项目: {project}")
    print(f"SVG 数量: {svg_count}")
    if errors:
        print("❌ 错误:")
        for e in errors:
            print(f"   - {e}")
    if warnings:
        print("⚠️  警告:")
        for w in warnings:
            print(f"   - {w}")
    if not errors and not warnings:
        print("✅ 校验通过，无错误无警告")


def cmd_info(args):
    project = _resolve_project_root(Path(args.project_path))
    meta_file = project / META_FILE
    if not meta_file.exists():
        print(f"错误：不是有效项目目录(缺 {META_FILE}): {project}", file=sys.stderr)
        return 1
    meta = json.loads(meta_file.read_text(encoding="utf-8"))
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    svgs = sorted((p.name for p in (project / "svg_output").glob("*.svg")))
    if svgs:
        print(f"SVG 文件: {', '.join(svgs)}")
    srcs = sorted((p.name for p in (project / "sources").iterdir() if p.is_file()))
    if srcs:
        print(f"源文件: {', '.join(srcs)}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog="project_manager.py",
        description="Diagram Master 轻量项目管理。",
    )
    sub = p.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="创建项目目录")
    p_init.add_argument("project_name", help="项目名(不含路径)")
    p_init.add_argument(
        "--format",
        default="1280x720",
        help="画布格式，如 1280x720 / 1920x720 / 1080x1080(默认 1280x720)",
    )
    p_init.set_defaults(func=cmd_init)

    p_imp = sub.add_parser("import-sources", help="导入源文件到 sources/")
    p_imp.add_argument("project_path", help="项目目录路径")
    p_imp.add_argument("files", nargs="+", help="要导入的源文件")
    p_imp.add_argument("--move", action="store_true", help="移动而非复制(默认推荐)")
    p_imp.set_defaults(func=cmd_import_sources)

    p_val = sub.add_parser("validate", help="校验项目结构")
    p_val.add_argument("project_path", help="项目目录路径")
    p_val.set_defaults(func=cmd_validate)

    p_info = sub.add_parser("info", help="打印项目元信息")
    p_info.add_argument("project_path", help="项目目录路径")
    p_info.set_defaults(func=cmd_info)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
