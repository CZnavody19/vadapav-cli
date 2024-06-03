from requests import get
from consts import file_svg_path, folder_svg_path

def get_html(url) -> str:
    return get(url).text

def join_url(url):
    return "https://vadapav.mov{}".format(url)

def fancy_title(title) -> str:
    out = ""
    for item in title.split("/")[1:]:
        out += "[cyan]/ [bold]{}[/bold][/cyan] ".format(item.strip())
    return out

def get_svg_type(svg_path) -> str:
    if svg_path == file_svg_path:
        return "file"
    elif svg_path == folder_svg_path:
        return "folder"
    else:
        return "unknown"
    
def get_readable_file_size(size) -> str:
    try:
        size = int(size)
    except:
        return "-"

    if size < 1024:
        return "{} B".format(size)
    elif size < 1024**2:
        return "{:.2f} KB".format(size/1024)
    elif size < 1024**3:
        return "{:.2f} MB".format(size/1024**2)
    elif size < 1024**4:
        return "{:.2f} GB".format(size/1024**3)
    else:
        return "{:.2f} TB".format(size/1024**4)