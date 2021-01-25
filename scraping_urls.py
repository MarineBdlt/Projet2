import requests
from bs4 import BeautifulSoup

urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"


def get_category_links(urlSite):
    """Return list of all categories"""

    reponse = requests.get(urlSite)
    soup = BeautifulSoup(reponse.text, "lxml")
    category_links = list()
    links = soup.find("div", "side_categories").ul.ul.find_all("li")
    for link in links:
        link = link.a.attrs["href"]
        finale_link = f"{urlSite}/{link}"
        category_links.append(finale_link)
    return category_links


def scrape_book_urls(category_url):
    """Scrap all books urls in a category"""

    reponse = requests.get(category_url)
    book_urls = []
    if reponse.ok:

        soup = BeautifulSoup(reponse.text, "lxml")
        for h3 in soup.findAll("h3"):
            book_a = h3.find("a")
            book_url = book_a["href"]
            full_book_url = base_url_for_categories + "/".join(book_url.split("/")[-2:])
            book_urls.append(full_book_url)

    return book_urls


def get_all_urls_pages(category_url):
    """Return urls of pages in a category"""

    urls_pages = list()
    reponse = requests.get(category_url)
    soup = BeautifulSoup(reponse.text, "lxml")
    category_url_base = category_url
    urls_pages.append(category_url)
    nb = 2
    while soup.select(".next > a"):
        category_url = category_url_base.replace("index", f"page-{nb}")
        reponse = requests.get(category_url)
        soup = BeautifulSoup(reponse.text, "lxml")
        nb += 1
        urls_pages.append(category_url)
    return urls_pages


def all_urls_books_in_category(category_url):
    """Return all books urls in a category"""

    liste_urls_books = []
    urls_pages = get_all_urls_pages(category_url)
    for url in urls_pages:
        scrap = scrape_book_urls(url)
        liste_urls_books.extend(scrap)
    return liste_urls_books
