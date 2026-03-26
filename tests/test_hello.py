import pytest
from hello import hello 

TARGET = "Hello World!"

def test_hello_prints(capysy: pytest.CaptureFixture[str]) -> None:
    captured = capsys.readouterr()
    assert captured.out == TARGET + "\n"


def test_hello_returns() -> None:
    result: str = hello()
    assert result == TARGET