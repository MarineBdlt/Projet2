# OC_Projet2_BooktoScrape
# Scraping d'une bibliothèque en ligne

Le projet est un programme pour extraire les informations suivantes de la librairie en ligne : books.toscrape.com

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

Ces informations sont enregistrées dans un fichier CSV pour chaque catégorie de livres et les images de couvertures de tous les livres sont également enregistrées dans le dossier "Images".

## Pour commencer

Ces instructions permettent d'obtenir une copie du projet afin de le tester sur votre machine.

### Pré-requis

Le programme étant écrit en Python, il est indispensable que celui-ci soit installé sur votre machine. Vous pouvez
* [télecharger Python](https://www.python.org/downloads/) - 

### Installation

Pour ne pas entrer en conflit avec d'autres projets déjà existants, il est préférable d'exécuter le programme sous un environnement virtuel.
Voici le sprincipales commandes pour :

1. Créer un environnement virtuel 
```python python3 -m venv tutorial-env```

2. Activer l'environnement virtuel

```python tutorial-env\Scripts\activate.bat```

Pour plus de détails sur l'installation d'un environnement virtuel, se reporter à la documentation Python
* [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/) - 

Il est également nécessaire d'installer les bibliothèques indispensables au bon fonctionnement du programme. Celles-ci sont listées dans le document ```python requirement.txt``` et leur installation se fait via la commande suivante exécutée dans l'environnement virtuel que vous venez de créer:

```python pip install -r requirements.txt```

## Démarrage

Une fois la console placée dans le dossier du programme, il suffit d'exécuter la commande suivante dans l'environnement virtuel:

```python python3 main.py```

Des dossiers ```python CSV``` et ```python Images``` vont se créer. Ils contiendront respectivement les fichiers CSV de chaque catégorie de livre ainsi que toutes les images de couverture. Vous pourrez suivre l'évolution du programme grâce à l'affichage de la catégorie en cours d'extraction sur la console.

## [![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)] [VisualStudioCode](https://code.visualstudio.com/) - Editeur de textes


## Auteurs
Listez le(s) auteur(s) du projet ici !
* **Marine BAP** _alias_ [@MarineBdlt](https://github.com/outout14)


## Remerciements

Merci à **Ranga Gonnage** pour son enseignement et son soutien.



