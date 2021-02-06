# OC_Projet2_BooktoScrape
# Scraping d'une bibliothèque en ligne

Le projet est un programme pour extraire les informations suivantes de la librairie en ligne [BooksToScrape](https:books.toscrape.com/) :

product_page_url

universal_ product_code (upc)

title

price_including_tax

price_excluding_tax

number_available

product_description

category

review_rating

image_url

Ces informations sont enregistrées dans un fichier CSV et dans un dossier Images pour chaque catégorie de livres.

## Pour commencer

Ces instructions permettent d'obtenir une copie du projet afin de le tester sur votre machine.

### Pré-requis

Le programme étant écrit en Python, il est indispensable que celui-ci soit installé sur votre machine. Vous pouvez télécharger Python :
* [Télecharger Python](https://www.python.org/downloads/)  

### Installation

Pour ne pas entrer en conflit avec d'autres projets déjà existants, il est préférable d'exécuter le programme sous un environnement virtuel.
Voici les principales commandes pour :

1. Créer un environnement virtuel 

```python3 -m venv tutorial-env```

2. Activer l'environnement virtuel

```tutorial-env\Scripts\activate.bat```

Pour plus de détails sur l'installation d'un environnement virtuel, se reporter à la documentation Python
* [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/)  

Il est également nécessaire d'installer les bibliothèques indispensables au bon fonctionnement du programme. Celles-ci sont listées dans le document ```requirement.txt``` et leur installation se fait via la commande suivante exécutée dans l'environnement virtuel que vous venez de créer:

```pip install -r requirements.txt```

## Démarrage

Une fois la console placée dans le dossier du programme, il suffit d'exécuter la commande suivante dans l'environnement virtuel:

```python3 main.py```

Des fichiers ```CSV``` et des dossiers ```Images``` vont se créer pour chaque catégorie de livres. Ils contiendront respectivement les fichiers CSV de tous les livres d'une catégorie ainsi que toutes les images de couverture relative à ces mêmes livres. 

Vous pourrez suivre l'évolution du programme grâce au pourcentage en cours d'extraction sur la console.

## Fabriqué avec
[VisualStudioCode](https://code.visualstudio.com/) - Editeur de textes


## Auteurs

* **Marine BAP** _alias_ [@MarineBdlt](https://github.com/outout14)


## Remerciements

Merci à **Ranga Gonnage** pour son enseignement et son soutien.



