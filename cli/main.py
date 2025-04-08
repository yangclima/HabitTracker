import typer

app = typer.Typer()

@app.command()
def hello():
    typer.echo("Habit Tracker CLI pronta!")

if __name__ == "__main__":
    app()
