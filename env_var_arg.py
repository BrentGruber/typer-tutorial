import typer

def main(name: str = typer.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"], show_envvar=True)):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)