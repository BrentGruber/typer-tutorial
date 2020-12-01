import typer

def main(name: str, lastname: str = typer.Option(...)):
    typer.echo()