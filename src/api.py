
"""API client functions for EmojiHub CLI.

Uses the public EmojiHub API documented at:
https://github.com/cheatsnake/emojihub

All functions raise RuntimeError with a helpful message on network or API errors.
"""
from __future__ import annotations
import requests
from typing import Any, Dict, List

BASE_URL = "https://emojihub.yurace.pro/api"

class EmojiHubError(RuntimeError):
    """Domain-specific error for EmojiHub failures."""
    pass

def _get(endpoint: str) -> Any:
    """Internal helper to GET JSON from EmojiHub.

    Parameters
    ----------
    endpoint : str
        Endpoint path starting with '/' (e.g., '/random')

    Returns
    -------
    Any
        Parsed JSON from the API.

    Raises
    ------
    EmojiHubError
        If the request fails, response is not JSON, or status is not OK.
    """
    url = BASE_URL + endpoint
    try:
        resp = requests.get(url, timeout=10)
    except requests.RequestException as exc:
        raise EmojiHubError(f"Network error contacting EmojiHub: {exc}") from exc

    if resp.status_code != 200:
        raise EmojiHubError(f"EmojiHub returned status {resp.status_code}: {resp.text[:120]}")

    try:
        return resp.json()
    except ValueError as exc:
        raise EmojiHubError("EmojiHub response was not valid JSON") from exc

def random_emoji() -> Dict[str, Any]:
    """Fetch a random emoji object."""
    return _get("/random")

def emoji_by_name(name: str) -> List[Dict[str, Any]]:
    """Fetch emojis by exact name (API treats hyphens/spaces variably).

    Examples of names: 'grinning face', 'skull', 'rolling on the floor laughing'
    Returns a list (can be empty) of emoji entries.
    """
    # API expects hyphenated; normalize user input.
    q = name.strip().lower().replace("_","-").replace(" ", "-")
    return _get(f"/all/name/{q}")

def by_category(category: str) -> List[Dict[str, Any]]:
    """Fetch emojis for a category, e.g. 'smileys-and-emotion'."""
    q = category.strip().lower().replace(" ", "-")
    return _get(f"/all/category/{q}")

def by_group(group: str) -> List[Dict[str, Any]]:
    """Fetch emojis for a group, e.g. 'face-smiling'."""
    q = group.strip().lower().replace(" ", "-")
    return _get(f"/all/group/{q}")
