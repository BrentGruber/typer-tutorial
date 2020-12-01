import typer

def main(name: str, lastname: str = typer.Option(..., prompt="Please share your last name"), email: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
    typer.echo(f"Hello {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)