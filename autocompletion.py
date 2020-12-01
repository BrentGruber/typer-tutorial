import typer

valid_names = [
    ("Brent", "The python guy"), 
    ("Tom", "The Reader of books"), 
    ("George", "The singer")
]

def complete_name(incomplete: str):
    for name, help_text in valid_names:
        if name.startswith(incomplete):
            yield (name, help_text)

def main(name: str = typer.Option("World", help="The name to say hi to.", autocompletion=complete_name)):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)