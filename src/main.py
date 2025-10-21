
"""CLI entry point for EmojiHub.

Run with:
    python -m src.main --help
"""
from __future__ import annotations
import argparse
from typing import Any, Dict, List
from . import api

def format_emoji(entry: Dict[str, Any]) -> str:
    """Pretty-print a single emoji entry from EmojiHub."""
    # Typical keys: name, category, group, htmlCode(list), unicode(list)
    name = entry.get("name", "unknown")
    category = entry.get("category", "unknown")
    group = entry.get("group", "unknown")
    unicodes = ", ".join(entry.get("unicode", [])[:3]) if isinstance(entry.get("unicode"), list) else ""
    html_codes = ", ".join(entry.get("htmlCode", [])[:2]) if isinstance(entry.get("htmlCode"), list) else ""
    return f"""{name}
• category: {category}
• group: {group}
• unicodes: {unicodes}
• html: {html_codes}"""

def cmd_random(_: argparse.Namespace) -> int:
    data = api.random_emoji()
    print(format_emoji(data))
    return 0

def cmd_get(args: argparse.Namespace) -> int:
    results = api.emoji_by_name(args.name)
    if not results:
        print(f"No emoji found for name: {args.name}")
        return 1
    for e in results:
        print(format_emoji(e))
        print()
    return 0

def cmd_category(args: argparse.Namespace) -> int:
    items = api.by_category(args.category)
    if not items:
        print(f"No emojis found for category: {args.category}")
        return 1
    for e in items[:args.limit]:
        print(format_emoji(e))
        print()
    return 0

def cmd_group(args: argparse.Namespace) -> int:
    items = api.by_group(args.group)
    if not items:
        print(f"No emojis found for group: {args.group}")
        return 1
    for e in items[:args.limit]:
        print(format_emoji(e))
        print()
    return 0

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="emojihub",
        description="CLI to explore emojis via the EmojiHub public API."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_random = sub.add_parser("random", help="Show a random emoji")
    p_random.set_defaults(func=cmd_random)

    p_get = sub.add_parser("get", help="Get emoji(s) by name (exact-ish match)")
    p_get.add_argument("name", help="Emoji name, e.g. 'skull' or 'grinning face'")
    p_get.set_defaults(func=cmd_get)

    p_cat = sub.add_parser("category", help="List emojis by category")
    p_cat.add_argument("category", help="e.g. 'smileys-and-emotion'")
    p_cat.add_argument("--limit", type=int, default=10, help="Max emojis to show")
    p_cat.set_defaults(func=cmd_category)

    p_group = sub.add_parser("group", help="List emojis by group")
    p_group.add_argument("group", help="e.g. 'face-smiling'")
    p_group.add_argument("--limit", type=int, default=10, help="Max emojis to show")
    p_group.set_defaults(func=cmd_group)

    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
