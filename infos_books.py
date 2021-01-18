import requests
import lxml
import csv
import string
import re
from bs4 import BeautifulSoup
import ast

urlSite = "http://books.toscrape.com"
base_url_for_categories = "http://books.toscrape.com/catalogue/"
urlBook = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

reponse = requests.get(urlBook)
soup = BeautifulSoup(reponse.text, "lxml")
soup2 = soup.find("article", "product_page")


def get_rating(soup):
    ps = soup.find_all("p")  # Soup sur toute la page. # Trouve tous les "p"
    p_rating = None  # Création d'un boléen pour rating
    for p in ps:  # Boucle qui parcours ps
        if (
            "star-rating" in p["class"]
        ):  # Si il y a "star rating" parmi les arguments "class" dans p
            p_rating = p["class"]  # Alors la variable p_rating corresponds à l'argument
            break  # Arreter la boucle
    assert p_rating is not None  # Verifier que p_rating a été trouvé
    letters_to_numbers = (
        {  # Création d'un dictionnaire # Attribution de clefs lettres aux chiffres
            "Zero": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }
    )
    rating = letters_to_numbers[
        p_rating[1]
    ]  # Création d'une variable qui insère les chiffres rating dans le dictionnaire (?)
    return rating


def get_category(soup):
    links = soup.findAll(
        "a"
    )  # Sortie du champ, soup sur toute la page. #Trouve tous les a
    category = None  # Création d'un boléen pour categorie
    for u in links:  # Boucle for qui parcoure les links (soit les "a")

        if (
            "category" in u["href"] and u.text != "Books"
        ):  # Si parmi les "a", le programme trouve "category" et "href" sans "books"
            category = u.text  # Alors extraire le texte correspondant
            break  # Arrêter la boucle
    assert (
        category is not None
    )  # Vérifier que category a été trouvée, relève une AssertionError si category = None
    return category


def get_description(soup2):
    description = soup2.find(
        "p", recursive=False
    )  # Au sein de ce champ, il trouve le dernier "p"
    return description.text


def get_image_url(soup2):
    image = soup2.find("img")  # Au sein de ce champ, il trouve "img"
    img_url = (urlSite + soup2.img["src"]).replace(
        "../..", ""
    )  # Création de la variable de l'url image
    return img_url


def get_title(soup):
    titre = (
        soup.find("title").get_text().strip().strip("\n").split("|")[0]
    )  # Création de la variable titre attribuée a "title", changée en text
    return titre


def set_th_infos(soup2, data_livre):
    tds = soup2.findAll("td")  # Au sein de ce champ, il trouve td
    ths = soup2.findAll("th")  # Au sein de ce champ, il trouve ths
    for td, th in zip(
        tds, ths
    ):  # Création d'une boucle pour chaque td (element), dans chaque th (iterable argument)
        data_livre[
            th.text
        ] = (
            td.text
        )  # Attribution du texte de td à une clef th text dans le dico (inutile?)


def get_book_info(urlBook):  # Définition de la fonction avec paramètre url
    data_livre = dict()  # Création du dictionnaire
    reponse = requests.get(urlBook)  # Chemin pour chercher l'url

    if reponse.ok:  # Si le programme get l'url
        soup = BeautifulSoup(
            reponse.content, "lxml"
        )  # Alors, il utilise BeautifulSoup et "lxml"
        soup2 = soup.find(
            "article", "product_page"
        )  # Champ de recherche plus restreint
        data_livre[
            "url"
        ] = urlBook  # Attribution du lien à la clef url dans le dictionnaire
        data_livre["title"] = get_title(
            soup
        )  # Ajout du titre du livre à l'indice "title" dans le dictionnaire
        data_livre["category"] = get_category(
            soup
        )  # Insertion de la category dans le dictionnaire global, associé à la clef "category"
        data_livre["rating"] = get_rating(soup2)
        data_livre["img_url"] = get_image_url(
            soup
        )  # Ajout de l'url image dans le dictionnaire avec la clef "img_url"
        data_livre["description"] = get_description(
            soup2
        )  # Ajout de la description dans le dico avec la clef "description"
        set_th_infos(soup2, data_livre)

    # Output : le dictionnaire des infos d'un livre
    return data_livre


# data_livre = ast.literal_eval(data_livre)

# Variable url du fichier


# Formatage du dico
