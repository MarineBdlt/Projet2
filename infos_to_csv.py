from infos_books import *
from books_urls_in_category import *
import requests
import lxml
import PIL
from PIL import Image


# Créer dossier avec nom de la catégorie
from pathlib import Path
from bs4 import BeautifulSoup


category_url = (
    "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
)
urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"

data_livre = get_book_info(urlBook)


def get_category_names(urlSite):
    """Renvoie la liste des catégories"""
    reponse = requests.get(urlSite)
    soup = BeautifulSoup(reponse.text, "lxml")
    category_names = list()
    links = soup.find_all(
        "a"
    )  # Sortie du champ, soup sur toute la page. #Trouve tous les a  # Création d'un boléen pour categorie
    for u in links:  # Boucle for qui parcoure les links (soit les "a")

        if (
            "category" in u["href"]
        ):  # Si parmi les "a", le programme trouve "category" et "href" sans "books"
            category = u.text  # Alors extraire le texte correspondant
            # Vérifier que category a été trouvée, relève une AssertionError si category = None
            category = category.replace("\n", "").replace(" ", "")
            category_names.append(category)
    category_names.pop(0)
    return category_names


def save_book_data_to_csvfile(category_url):
    """Enregistre les infos des livres d'une catégorie dans fichier excel"""
    path = Path(".", "data")
    path.mkdir(exist_ok=True)
    url_first_book = all_urls_in_category(category_url)[0]
    first_book = get_book_info(url_first_book)
    category_name = first_book["category"]
    category_path = Path(path, category_name)
    category_path.mkdir(exist_ok=True)
    filepath = Path(category_path, f"{category_name}.csv")
    with filepath.open("w", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=first_book.keys(), dialect="excel")
        writer.writeheader()
        for url in all_urls_in_category(category_url):
            all_data = get_book_info(url)
            writer.writerow(all_data)


def scrap_images_in_category(category_url, urlSite):
    reponse_category = requests.get(category_url)
    soup3 = BeautifulSoup(reponse_category.text, "lxml")
    list_images = []
    for img in soup3.find_all("img"):
        halflink = img["src"]
        list_images.append(halflink.replace("../../../..", urlSite))
    return list_images


scrap_images_in_category(category_url, urlSite)

# http://books.toscrape.com/media/cache/9b/09/9b0935dc936c92900c2dc5d2114da72f.jpg


scrap_images_in_category(category_url, urlSite)


def save_images_to_file(category_url, urlSite):

    path = Path(".", "data")
    path.mkdir(exist_ok=True)
    url_first_book = all_urls_in_category(category_url)[0]
    first_book = get_book_info(url_first_book)
    category_name = first_book["category"]
    category_path = Path(path, category_name)
    category_path.mkdir(exist_ok=True)

    img_path = Path(category_path, f"{category_name}-images")
    img_path.mkdir(exist_ok=True)

    i = 0

    for url in scrap_images_in_category(category_url, urlSite):
        print(url)
        content = requests.get(url).content
        filepath = Path(img_path, f"{i}.jpg")
        with filepath.open("wb") as jpgfile:
            jpgfile.write(content)
        i += 1
    """Enregistre les images dans fichier à l'intérieur d'une catégorie"""
    # request images


save_images_to_file(category_url, urlSite)
# fonction jpg

# écrire le headers QUE si le fichier est vide : if
# mettre le path

'''
soup = BeautifulSoup(reponse.text, "lxml")
soup2 = soup.find("article", "product_page")
def get_rating(soup):
    ps = soup.find_all("p")  # Soup sur toute la page. # Trouve tous les "p"
    p_rating = None 

    <article class="product_pod">
        
            <div class="image_container">
                
                    
                    <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"><img src="media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg" alt="The Dirty Little Secrets of Getting Your Dream Job" class="thumbnail"></a>
                    
                
            </div>
        

        
            
                <p class="star-rating Four">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>


def creation_dossiers(urlSite):
    """Crée un dossier par catégorie"""
    n = 2
    for name in get_category_names(urlSite):
        p = pathlib.Path("categories/" + name)
        p.mkdir(parents=True, exist_ok=True)
        category_url = (
            base_url_for_categories
            + "category/"
            + "books/"
            + name.lower()
            + "_"
            + str(n)
            + "/index.html"
        )


# créer un dossier par catégorie (FAIT?)

# puis aller dans chaque dossier pour créer le fichier csv


def save_books_info_to_csv(urlSite):
    """Enregistre les infos d'un livre dans fichier excel"""
    i = 1
    n = 2
    name_list = get_category_names(urlSite)
    for name in name_list:
        category_url = (
            base_url_for_categories
            + "category/"
            + "books/"
            + name.lower()
            + "_"
            + str(n)
            + "/index.html"
        )
        return category_url
        n += 1
        while i < 50:
            p = pathlib.touch(
                "TEST/" + str(name_list[i].lower()) + "/"
            )  # pathlib path ? # #
            p.mkdir(parents=True, exist_ok=True)
            fn = ""
            filepath = p / fn
        with open(f"{name_list[i]}.csv", "w", encoding="utf-8-sig") as csvfile:
            for url in all_urls_in_category(category_url):
                all_data = get_book_info(url)
                print("\n\n", url, nb, "\n\n", all_data)
                writer = csv.DictWriter(csvfile, all_data, dialect="excel")
                writer.writeheader()
                writer.writerow(all_data)
        i += 1


# save_books_info_to_csv(urlSite)


creation_dossiers(urlSite)
p = pathlib.Path("categories/" + str(c) + "/")
        p.mkdir(parents=True, exist_ok=True)
        fn = ""
        filepath = p / fn
        with filepath.open("w", encoding="utf-8") as f:
            f.write(str(dict))

creation_dossiers(urlSite)
p = pathlib.Path("categories/" + str(c) + "/")
        p.mkdir(parents=True, exist_ok=True)
        fn = ""
        filepath = p / fn
        with filepath.open("w", encoding="utf-8") as f:
            f.write(str(dict))


def creation_dossiers(urlSite):
    """Crée un dossier par catégorie"""
    n = 2
    for name in get_category_names(urlSite):
        p = pathlib.Path("categories/" + name)
        p.mkdir(parents=True, exist_ok=True)
        category_url = (
            base_url_for_categories
            + "category/"
            + "books/"
            + name.lower()
            + "_"
            + str(n)
            + "/index.html"
        )
        n += 1
        fn = ""
        filepath = p / fn

    with filepath.open(f"{name}.csv", "w", encoding="utf-8-sig") as csvfile:
        for url in all_urls_in_category(category_url):
            all_data = get_book_info(url)
            print("\n\n", url, nb, "\n\n", all_data)
            writer = csv.DictWriter(csvfile, all_data, dialect="excel")
            writer.writeheader()
            writer.writerow(all_data)
            print(category_url)  # save_books_info_to_csv()


# faire marcher le code
# Ou separer en deux codes : un qui crée les fichiers, un qui écrit dedans ?
# créer un fichier image avec toutes les images des livres, dans chaque catégorie

# categorie
# fichier csv
# data livres
# fichier images
# images livres   # 1. Creer path pour ranger une image dans un fichier 2. Mettre toutes les images dedans

naviguer dans les fichiers
>>> p = Path('/etc')
>>> q = p / 'init.d' / 'reboot'
>>> q
PosixPath('/etc/init.d/reboot')
>>> q.resolve()
PosixPath('/etc/rc.d/init.d/halt')

ouvrir et fermer un fichier

>>> p = Path('my_text_file')
>>> p.write_text('Text file contents')
18
>>> p.read_text()
'Text file contents'

creation_dossiers(urlSite)
p = pathlib.Path("categories/" + str(c) + "/")
        p.mkdir(parents=True, exist_ok=True)
        fn = ""
        filepath = p / fn
        with filepath.open("w", encoding="utf-8") as f:
            f.write(str(dict))

def save_books_info_to_csv(category_url):
    """Enregistre les infos d'un livre dans fichier excel"""
    with open(f'{"FantastiqueWESH"}.csv', "w", encoding="utf-8-sig") as csvfile:
        for url in all_urls_in_category(category_url):
            all_data = get_book_info(url)
            print("\n\n", url, nb, "\n\n", all_data)
            writer = csv.DictWriter(csvfile, all_data, dialect="excel")
            writer.writeheader()
            writer.writerow(all_data)
'''

"""
def dossiers_categories_names(url, fn):
    for c in categories_names:
        p = pathlib.Path("categories/" + str(c) + "/")
        p.mkdir(parents=True, exist_ok=True)
        fn = ""
        filepath = p / fn
        with filepath.open("w", encoding="utf-8") as f:
            f.write(str(dict))


creation_dossiers(urlSite)
# http://books.toscrape.com/catalogue/category/books/crime_51/index.html

category_url = (
    "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
)
urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"

data_livre = get_book_info(urlBook)
# pour chaque url mettre le nom de l'url pour le fichier
# mettre le fichier dans un dossier catégorie


# save_book_info_to_csv(category_url)


with open(f'{data_livre["data"]}.csv', "w", encoding="utf-8-sig") as csvfile:
# Vidéo Thierry, corriger le prix html



def all_data_books_in_category(category_url):
    nb = 0
    for url in all_urls_in_category(category_url):
        nb += 1
        all_data = get_book_info(url)
        save_book_info_to_csv(all_data)
        print("\n\n", url, nb, "\n\n", data_livre)


all_data_books_in_category(category_url)



import pandas as pd

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
et si vous voulez l'exporter vers un seul fichier csv, utilisez ceci:

combined_csv.to_csv( "combined_csv.csv", index=False )


def all_books_to_csv(category_url):
    save_book_info_to_csv(get_book_info(all_urls_in_category(category_url)))
    print("OK")



def dossiers_categories_names(url, fn):
    for c in categories_names:
        p = pathlib.Path("categories/" + str(c) + "/")
        p.mkdir(parents=True, exist_ok=True)
        fn = ""
        filepath = p / fn
        with filepath.open("w", encoding="utf-8") as f:
            f.write(str(dict))


dossiers_categories_names()



import pathlib

p = pathlib.Path("categories/")
p.mkdir(parents=True, exist_ok=True)
fn = "categoryphilo.txt"  # sous dossiers catégories avec noms
# dans chaque dossier # fichier csv + fichier image
filepath = p / fn
with filepath.open("w", encoding="utf-8") as f:
    f.write("blabla")

save_book_info_to_csv(data_livre)
"""
