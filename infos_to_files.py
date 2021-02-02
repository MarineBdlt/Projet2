import infos_books
import scraping_urls

import requests
import lxml
import csv
from tqdm import tqdm

import urllib
import urllib.request
import csv

from pathlib import Path
from bs4 import BeautifulSoup


urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"


def save_book_data_to_csvfile(category_url):
    """Save the data of all books in a category in a csv file"""

    path = Path(".", "data")
    path.mkdir(exist_ok=True)

    url_first_book = scraping_urls.all_urls_books_in_category(category_url)[0]

    first_book = infos_books.get_book_info(url_first_book)
    category_name = first_book["category"]
    category_path = Path(path, category_name)
    category_path.mkdir(exist_ok=True)
    filepath = Path(category_path, f"{category_name}.csv")
    with filepath.open("w", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=first_book.keys(), dialect="excel")
        writer.writeheader()
        for url in scraping_urls.all_urls_books_in_category(category_url):
            all_data = infos_books.get_book_info(url)
            writer.writerow(all_data)


def all_data(category_url):
    """ Put in a list all data in a category """

    all_data = []
    for url in scraping_urls.all_urls_books_in_category(category_url):
        all_data.append(infos_books.get_book_info(url))
    return all_data


def liste_tuples_images(all_data):
    """ Create a tuples list (image, titre) for each book """

    liste = []
    for data_row in all_data:

        liste.append((data_row["img_url"], data_row["title"]))

    return liste


def save_images_to_file(category_url):
    """ Save all books images from a category """

    all_data_var = all_data(category_url)
    liste_tuples = liste_tuples_images(all_data_var)
    path = Path(".", "data")
    path.mkdir(exist_ok=True)
    url_first_book = scraping_urls.all_urls_books_in_category(category_url)[0]
    first_book = infos_books.get_book_info(url_first_book)
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
