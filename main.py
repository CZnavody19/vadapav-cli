from html_parser import parse_items, parse_title
from utils import get_html, fancy_title, get_readable_file_size
from validator import validate_url
from rich import print
from rich.prompt import Prompt
from rich.table import Table

def get_args() -> dict:
    out = {}

    url = Prompt.ask("[magenta bold]Enter the URL[/magenta bold]")
    if not validate_url(url):
        print("[red]Invalid URL. Exiting.[/red]")
        exit(1)
    out["url"] = url

    return out

def main(args: dict):
    html = get_html(args["url"])
    title = parse_title(html)
    items = parse_items(html)[1:]

    table = Table(title=fancy_title(title))
    table.add_column("Type", justify="left", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Size", justify="right", style="green")

    for item in items:
        table.add_row(item["type"], item["name"], get_readable_file_size(item["size"]))

    print()
    print(table)
    print("Total: [bold green]{}[/bold green] items [{}]".format(len(items), get_readable_file_size(sum([i["size"] for i in items]))))
    print()

    file = Prompt.ask("[magenta bold]Enter the file name[/magenta bold]")
    with open(file if file != "" else "out.txt", "w") as f:
        f.write("\n".join([i["url"] for i in items]))

if __name__ == "__main__":
    args = get_args()
    main(args=args)