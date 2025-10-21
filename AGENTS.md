
# AGENTS.md — Context for AI Assistants

## Overview
Build a Python CLI that explores emojis via the EmojiHub API. Provide 3+ subcommands, tests with mocking, CI via GitHub Actions, and professional docs.

## API
- Base: https://emojihub.yurace.pro/api
- Endpoints used:
  - `/random`
  - `/all/name/{name-hyphenated}`
  - `/all/category/{category}`
  - `/all/group/{group}`

## CLI Commands
- `random`
- `get <name>`
- `category <category> [--limit N]`
- `group <group> [--limit N]`

## Files
- src/api.py: API functions with error handling
- src/main.py: argparse CLI
- tests/: pytest files mocking requests / API functions
- .github/workflows/tests.yml: run pytest on push/PR
- requirements.txt, README.md

## Standards
- PEP8, docstrings
- No real HTTP in tests (mock requests.get)
