from scrap_infos_books import *
from scraping_urls import *
import requests
import lxml
import PIL
from PIL import Image
import urllib
import urllib.request


# Créer dossier avec nom de la catégorie
from pathlib import Path
from bs4 import BeautifulSoup


urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"

data_livre = get_book_info(urlBook)


def save_book_data_to_csvfile(category_url):
    """Enregistre les infos des livres d'une catégorie dans fichier excel"""
    path = Path(".", "data")
    path.mkdir(exist_ok=True)

    print(category_url)

    url_first_book = all_urls_books_in_category(category_url)[0]

    first_book = get_book_info(url_first_book)
    category_name = first_book["category"]
    category_path = Path(path, category_name)
    category_path.mkdir(exist_ok=True)
    filepath = Path(category_path, f"{category_name}.csv")
    with filepath.open("w", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=first_book.keys(), dialect="excel")
        writer.writeheader()
        for url in all_urls_books_in_category(category_url):
            all_data = get_book_info(url)
            writer.writerow(all_data)


def all_data(category_url):
    all_data = []
    for url in all_urls_books_in_category(category_url):
        all_data.append(get_book_info(url))
    return all_data


def liste_tuples_images(all_data):
    liste = []
    for data_row in all_data:

        liste.append((data_row["img_url"], data_row["title"]))

    return liste


def scrap_images_in_category(category_url, urlSite):
    reponse_category = requests.get(category_url)
    soup3 = BeautifulSoup(reponse_category.text, "lxml")
    list_images = []
    for img in soup3.find_all("img"):
        halflink = img["src"]
        list_images.append(halflink.replace("../../../..", urlSite))
    return list_images


def save_images_to_file(category_url):
    """sauve les images dans fichier"""
    all_data_var = all_data(category_url)
    liste_tuples = liste_tuples_images(all_data_var)
    path = Path(".", "data")
    path.mkdir(exist_ok=True)
    url_first_book = all_urls_books_in_category(category_url)[0]
    first_book = get_book_info(url_first_book)
    category_name = first_book["category"]
    category_path = Path(path, category_name)
    category_path.mkdir(exist_ok=True)

    img_path = Path(category_path, f"{category_name}-images")
    img_path.mkdir(exist_ok=True)

    for un_tuple in liste_tuples:

        image, title = un_tuple
        title = title.replace(" ", "_").replace("/", "_")

        filepath = Path(img_path, f"{title}.jpg")

        with filepath.open("wb") as jpgfile:
            jpgfile.write(urllib.request.urlopen(image).read())
