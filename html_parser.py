from bs4 import BeautifulSoup
from utils import get_svg_type, join_url

def parse_title(html):
    parsed = BeautifulSoup(html, features="html.parser")
    extracted = parsed.body.find("div", attrs={'class':'directory'}).find("div")
    return extracted.text.replace("\n", "").strip()

def parse_items(html):
    parsed = BeautifulSoup(html, features="html.parser")
    extracted = parsed.body.find("div", attrs={'class':'directory'}).find("ul").find_all("li")
    items = []
    for i in extracted:
        li_div = i.find("div", attrs={'class':'centerflex name-div'})
        if li_div:
            size_div = i.find("div", attrs={'class':'size-div'})
            li_a = li_div.find("a")
            li_svg = li_div.find("path")
            items.append({"url": join_url(li_a["href"]), "name": li_a.text, "type": get_svg_type(li_svg["d"]), "size": int(size_div.text) if size_div else 0})

    return items