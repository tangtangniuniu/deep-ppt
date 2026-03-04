"""Basic tests for deep-ppt."""

from click.testing import CliRunner

from deep_ppt import __version__
from deep_ppt.cli import main


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_cli_version() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_cli_generate_placeholder() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["generate", "Test Topic"])
    assert result.exit_code == 0
    assert "Test Topic" in result.output
