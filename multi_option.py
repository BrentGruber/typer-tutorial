from typing import List

import typer

valid_completion_items = [
    ("Brent", "The python guy"), 
    ("Tom", "The Reader of books"), 
    ("George", "The singer")
]

def complete_name(ctx, typer.Context, incomplete: str):
    names = ctx.params.get("name") or []
    for name, help_text in valid_completion_items:
        if name.startswith(incomplete) and name not in names:
            yield (name, help_text)

def main(name: List[str] = typer.Option(["World"], help="The name to say hi to.", autocompletion=complete_name)):
    for each_name in name:
        typer.echo(f"Hello {each_name}")
    
if __name__ == "__main__":
    typer.run(main)