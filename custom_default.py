import typer

def main(name: str = typer.Argument("Wade Wilson", metavar="✨Deadpool's name✨", help="Who to greet", show_default="Deadpoolio is the cooliest")):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)