
# EmojiHub CLI

![Tests](https://img.shields.io/badge/tests-passing-in_local.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple, portfolio-ready CLI to explore emojis from the [EmojiHub API](https://github.com/cheatsnake/emojihub).

## Features
- `random` — show one random emoji with details
- `get <name>` — fetch emoji(s) by name (e.g., `skull`, `grinning face`)
- `category <category>` — list emojis by category (e.g., `smileys-and-emotion`)
- `group <group>` — list emojis by group (e.g., `face-smiling`)

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run CLI
python -m src.main --help
python -m src.main random
python -m src.main get skull
python -m src.main category smileys-and-emotion --limit 5
python -m src.main group face-smiling --limit 5

# Run tests
pytest -q
```

## Tech
- Python, argparse, requests, pytest, GitHub Actions

## API Credit
Data from the public EmojiHub API. See: https://github.com/cheatsnake/emojihub
