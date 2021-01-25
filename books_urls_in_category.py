import requests
import time
from bs4 import BeautifulSoup

category_url = (
    "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
)
urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"


def get_category_links(urlSite):
    """Renvoie la liste des catégories"""
    reponse = requests.get(urlSite)
    soup = BeautifulSoup(reponse.text, "lxml")
    category_links = list()
    links = soup.find_all(
        "a"
    )  # Sortie du champ, soup sur toute la page. #Trouve tous les a  # Création d'un boléen pour categorie
    index = 0
    for u in links:
        # Boucle for qui parcoure les links (soit les "a")

        if (
            "category" in u["href"]
        ):  # Si parmi les "a", le programme trouve "category" et "href" sans "books"
            category = u.text.lower()  # Alors extraire le texte correspondant
            # Vérifier que category a été trouvée, relève une AssertionError si category = None
            category = category.replace("\n", "").replace(" ", "")
            category_links.append(
                base_url_for_categories
                + "category/books/"
                + category
                + "_"
                + str(index - 1)
                + "/index.html"
            )
        index += 1
    category_links.pop(0)
    return category_links


def scrape_book_urls(category_url):
    """Scrape toutes les urls des livres d'une page."""
    reponse = requests.get(category_url)
    book_urls = []
    if reponse.ok:

        soup = BeautifulSoup(reponse.text, "lxml")  # essentiel ?
        for h3 in soup.findAll("h3"):
            book_a = h3.find("a")

            # assert book_a.text == book_a["title"]
            book_url = book_a["href"]
            full_book_url = base_url_for_categories + "/".join(book_url.split("/")[-2:])
            book_urls.append(full_book_url)

    return book_urls  # return book_urls


# ressources exemple

nb = None
category_url = (
    "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
)

urls_pages = list()


def tourne_la_page(category_url):
    """Renvoie les urls des différentes pages d'une catégorie"""
    reponse = requests.get(category_url)
    soup = BeautifulSoup(reponse.text, "lxml")
    category_url_base = category_url
    nb = 1
    while soup.select(".next > a"):
        category_url = category_url_base.replace("index", f"page-{nb}")
        reponse = requests.get(category_url)
        soup = BeautifulSoup(reponse.text, "lxml")
        nb += 1
        urls_pages.append(category_url)
    return urls_pages


def all_urls_in_category(category_url):
    """Liste toutes les urls des livres d'une catégorie."""
    liste_urls_books = []
    urls_pages = tourne_la_page(category_url)
    for url in urls_pages:
        scrap = scrape_book_urls(url)
        liste_urls_books.extend(scrap)
    return liste_urls_books
