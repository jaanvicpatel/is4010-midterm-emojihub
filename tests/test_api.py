
import pytest
from unittest.mock import patch, MagicMock
from src import api

@patch('src.api.requests.get')
def test_random_emoji_ok(mock_get):
    m = MagicMock()
    m.status_code = 200
    m.json.return_value = {"name":"skull","category":"smileys-and-emotion","group":"face-neutral-skeptical","unicode":["U+1F480"],"htmlCode":["&#128128;"]}
    mock_get.return_value = m
    data = api.random_emoji()
    assert data["name"] == "skull"

@patch('src.api.requests.get')
def test_emoji_by_name_network_error(mock_get):
    # Simulate network exception
    import requests
    mock_get.side_effect = requests.RequestException("boom")
    with pytest.raises(api.EmojiHubError):
        api.emoji_by_name("skull")

@patch('src.api.requests.get')
def test_by_category_non_200(mock_get):
    m = MagicMock()
    m.status_code = 404
    m.text = "not found"
    mock_get.return_value = m
    with pytest.raises(api.EmojiHubError):
        api.by_category("smileys-and-emotion")
