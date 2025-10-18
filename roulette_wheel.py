#!/usr/bin/env python3
"""
Roulette Wheel Simulator CLI.

This program simulates spins on a European roulette wheel
and displays the color distribution or number frequencies.

Usage Examples:
    python roulette_wheel.py --count 1000
    python roulette_wheel.py --count 500 --color red
    ./roulette --count 2000 --color black
    ./roulette -c 100 -n green
    """

import random
from collections import Counter
import click


def color_of(number: int) -> str:
    """Return the color for a European roulette number (0..36)."""
    if number == 0:
        return "green"
    # Standard European mapping:
    # 1–10 & 19–28: odd -> red, even -> black
    # 11–18 & 29–36: odd -> black, even -> red
    if (1 <= number <= 10) or (19 <= number <= 28):
        return "red" if number % 2 == 1 else "black"
    return "black" if number % 2 == 1 else "red"


@click.command()
@click.option(
    "--count",
    "-c",
    default=1,
    type=int,
    show_default=True,
    help="Number of spins to simulate (must be >= 1).",
)
@click.option(
    "--color",
    "-n",
    type=click.Choice(["all", "red", "black", "green"], case_sensitive=False),
    default="all",
    show_default=True,
    help="Filter results by color (choose red, black, green, or all).",
)
def main(count: int, color: str) -> None:
    """Simulate COUNT spins of a European roulette wheel and print statistics."""
    if count < 1:
        raise click.BadParameter("count must be >= 1", param_hint="--count")

    # Simulate spins (0..36)
    spins = random.choices(range(37), k=count)
    number_counts = Counter(spins)
    color_counts = Counter(color_of(num) for num in spins)

    click.echo(f"Simulated {count} spins.")
    click.echo("Color distribution:")
    for color_name in ("red", "black", "green"):
        color_count = color_counts.get(color_name, 0)
        click.echo(
            f"  {color_name.title():6}: {color_count:6d} ({color_count / count * 100:5.2f}%)"
        )

    click.echo("")  # blank line

    if color.lower() != "all":
        target_color = color.lower()
        click.echo(f"Numbers with color '{target_color}':")
        numbers = [num for num in range(37) if color_of(num) == target_color]
        for num in numbers:
            num_count = number_counts.get(num, 0)
            click.echo(f"  {num:2d}: {num_count:6d} ({num_count / count * 100:5.2f}%)")
    else:
        click.echo("Top spun numbers:")
        for num, num_count in number_counts.most_common(10):
            click.echo(
                f"  {num:2d} ({color_of(num):5}): {num_count:6d} ({num_count / count * 100:5.2f}%)"
            )


if __name__ == "__main__":
    # Click handles the parameters automatically, so call without arguments
    main()  # pylint: disable=no-value-for-parameter
