"""CLI entry point for deep-ppt."""

import click

from deep_ppt import __version__


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """deep-ppt: Input a topic, get an editable, in-depth presentation."""


@main.command()
@click.argument("topic")
@click.option("--pages", default=20, help="Target number of slides")
@click.option("--lang", default="en", help="Output language (en/zh)")
@click.option("--output", "-o", default=None, help="Output file path")
def generate(topic: str, pages: int, lang: str, output: str | None) -> None:
    """Generate a presentation from a topic."""
    if output is None:
        safe_name = topic[:30].replace(" ", "_").lower()
        output = f"{safe_name}.pptx"

    click.echo(f"Topic: {topic}")
    click.echo(f"Target pages: {pages}")
    click.echo(f"Language: {lang}")
    click.echo(f"Output: {output}")
    click.echo("---")
    click.echo("Pipeline not yet implemented. Coming soon.")


if __name__ == "__main__":
    main()
