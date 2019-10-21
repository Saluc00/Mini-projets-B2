# Documentation du projet `Algo 1`

# Sommaire

- [Sujet](#sujet)
    - [Basic](#basic-✅)
    - [Allez plus loin](#allez-plus-loin-✅)
- [Informations](#informations)
- [Ressources](#ressources)
    - [Modules](#modules)
    - [Site web](#site-web)
- [Documentation](#documentation)
    - [Objet](#objet)
        - [Parcours](#parcours)
            - [Fonctions de l'objet parcours](#fonctions-de-lobjet-parcours)
    - [Fonctions Principales](#fonctions-principales)

# Sujet

Je suis un directeur d’entreprise de livraison routier à travers la France.

**Écrire  un  programme  qui  affiche  un  tableau  me  permettant  de  connaître  l'heure  à  laquelle  une livraison sera effectuée.**

- Un camion accélère de 10km/h, par minute.
- Un camion ralenti de 10km/h, par minute.
- Sa vitesse maximale est de 90 km/h.
- Un conducteur doit faire une pause de 15 min toutes les 2 heures.

### Basic ✅

*Écrire un programme qui :*

- Demande une ville de départ et une ville d’arrivée
- retourne un tableau avec : 
    - le nom de la ville de départ
    - le nom de la ville d’arrivée
    - la distance parcourue
    - le temps pour parcourir cette distance HH/mm (arrondi à la minute supérieure)
    
### Allez plus loin ✅

Améliorez le programme en permettant de faire plusieurs livraisons.
Lors d’une étape, un conducteur s’arrête 45 minutes

*Écrire un programme qui :*

- demande une ville de départ
- une/plusieurs ville(s) étapes et ville d’arrivée
- retourne un tableau avec :
    - le nom de laville de départ(par étapes)
    - le nom de la ville d’arrivée(par étapes)-la distance parcourue(par étapes)
    - le temps pour parcourir cette distance HH:mm (par étapes arrondis à la minute supérieure)
    - la distance totale parcourue
    - le tempstotal écoulé du départ à la dernière ville.

# Informations

*Se repository comporte deux fichiers*

######  Ils répondent chacun même à la demande du sujet, seulement, l'un est en objet allors alors que le second est un script. 
- `algo_script.py` *(script)*
- `algo_objet.py` *(objet)*

# Ressources

### Modules

Les modules utilisés sont :

- `BS4`
- `Requests`

Il est possible de les installer en **clonant le repo** et d'effectuer la commande `pip install -r requirements.txt` une fois placé dans le dossier où est cloné le projet.

### Site web

Pour récuperer les données j'utilise le site web:

```
https://www.bonnesroutes.com/widget/v1/html
```

# Documentation

### Objet

Le fichier `algo_objet.py` est le seul fichier à contenir un objet.

###### Parcours

L'objet **Parcours** est instancié avec aucun paramètre et pourtant, lorsqu'il est initialisé il demande une action de notre part.

Dans sont constructeur, il demande d'entrer des *adresses et/ou villes* autant de fois que vous le souhaitez tant que vous n'entrez pas ***stop***.

###### Fonctions de l'objet parcours

- [main](#main)
- [data](#data)
- [__repr__](#repr)

###### main

- **Main** est une fonction qui prend un seule paramètre qui doit etre un tableau contenant uniquement des chaînes de caractères.

- Si le parametre de main est un tableau comprenant 2 chaine de caractere la fonction retourne un tableau qui comprend *(dans cette ordre)*: 
    - La ville de départ
    - La ville d'arrivé
    - Le nombre de km parcourue
    - Le temps pour réaliser l'itinéraire

- Si le parametre de main est un tableau comprenant plus de 2 chaine de caractere la fonction retourne un tableau qui comprend *(dans cette ordre)*: 
    

###### data

###### __ repr __

### Fonctions Principales

