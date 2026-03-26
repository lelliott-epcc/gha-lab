import pytest
from hello import hello 

TARGET = "Hello World!"

def test_hello_prints(capsys: pytest.CaptureFixture[str]) -> None:
    hello()
    captured = capsys.readouterr()
    assert captured.out == TARGET


def test_hello_returns() -> None:
    result: str = hello()
    assert result == TARGET