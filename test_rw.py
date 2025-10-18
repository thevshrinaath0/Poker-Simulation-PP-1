"""Test suite for the roulette wheel simulator CLI."""

import pytest
from click.testing import CliRunner
from roulette_wheel import main, color_of


@pytest.mark.parametrize(
    "number,expected_color",
    [
        (0, "green"),
        (1, "red"),
        (2, "black"),
        (12, "red"),
        (19, "red"),
        (20, "black"),
        (36, "red"),
    ],
)
def test_color_of(number, expected_color):
    """Test that color_of() returns the correct color for a roulette number."""
    assert color_of(number) == expected_color


def test_cli_default_count():
    """Test CLI with default count=1 and color='all'."""
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Simulated 1 spins." in result.output


def test_cli_custom_count():
    """Test CLI with custom count=100 and color='red'."""
    runner = CliRunner()
    result = runner.invoke(main, ["--count", "100", "--color", "red"])
    assert result.exit_code == 0
    assert "Color distribution:" in result.output
    assert "Numbers with color 'red':" in result.output


def test_cli_invalid_count():
    """Test CLI with invalid count=0 should fail."""
    runner = CliRunner()
    result = runner.invoke(main, ["--count", "0"])
    assert result.exit_code != 0
    assert "count must be >= 1" in result.output
