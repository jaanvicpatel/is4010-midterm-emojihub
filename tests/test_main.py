
from unittest.mock import patch, MagicMock
import builtins
from src.main import build_parser

@patch('src.api.random_emoji')
def test_cli_random_prints(mock_random, capsys):
    mock_random.return_value = {"name":"skull","category":"smileys-and-emotion","group":"face-neutral-skeptical","unicode":["U+1F480"],"htmlCode":["&#128128;"]}
    parser = build_parser()
    args = parser.parse_args(["random"])
    # call bound function
    rc = args.func(args)
    assert rc == 0
    out = capsys.readouterr().out
    assert "skull" in out

@patch('src.api.emoji_by_name')
def test_cli_get_handles_no_results(mock_get, capsys):
    mock_get.return_value = []
    parser = build_parser()
    args = parser.parse_args(["get","no-such-emoji"])
    rc = args.func(args)
    assert rc == 1
    assert "No emoji found" in capsys.readouterr().out
