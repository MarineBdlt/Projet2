import requests
import lxml
from bs4 import BeautifulSoup

urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"
urlBook = "https://books.toscrape.com/catalogue/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html"

reponse = requests.get(urlBook)
soup = BeautifulSoup(reponse.text, "lxml")
soup2 = soup.find("article", "product_page")


def get_rating(soup):
    ps = soup.find_all("p")
    p_rating = None

    for p in ps:
        if "star-rating" in p["class"]:
            p_rating = p["class"]
            break
    assert p_rating is not None
    letters_to_numbers = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
    rating = letters_to_numbers[p_rating[1]]
    return rating


def get_category(soup):
    links = soup.findAll("a")
    category = None

    for u in links:
        if "category" in u["href"] and u.text != "Books":
            category = u.text
            break
    assert category is not None
    return category


def get_description(soup2):
    try:
        description = soup2.find("p", recursive=False)
        return description.text
    except AttributeError:
        return str("Il n'y a pas de description.")


def get_image_url(soup2):
    image = soup2.find("img")
    img_url = (urlSite + soup2.img["src"]).replace("../..", "")
    return img_url


def get_title(soup):
    titre = soup.find("title").get_text().strip().strip("\n").split("|")[0]
    return titre


def set_th_infos(soup2, data_livre):
    tds = soup2.findAll("td")
    ths = soup2.findAll("th")
    for td, th in zip(tds, ths):
        data_livre[th.text] = td.text


def get_book_info(urlBook):
    """Scrap all one book's informations"""

    data_livre = dict()
    reponse = requests.get(urlBook)

    if reponse.ok:
        soup = BeautifulSoup(reponse.content, "lxml")
        soup2 = soup.find("article", "product_page")
        data_livre["url"] = urlBook
        data_livre["title"] = get_title(soup)
        data_livre["category"] = get_category(soup)
        data_livre["rating"] = get_rating(soup2)
        data_livre["img_url"] = get_image_url(soup)
        data_livre["description"] = get_description(soup2)
        set_th_infos(soup2, data_livre)
    return data_livre
