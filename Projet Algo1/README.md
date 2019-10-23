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
    - [Fonctions Principales](#fonctions-principales)
        - [Main](#main)
        - [Data](#data)
        - [Repr](#repr)
        - [Pause](#pause)
        - [Tous](#tous)

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

## Objet

Le fichier `algo_objet.py` est le seul fichier à contenir un objet.

### Parcours

L'objet **Parcours** est instancié avec aucun paramètre et pourtant, lorsqu'il est initialisé il demande une action de notre part.

Dans sont constructeur, il demande d'entrer des *adresses et/ou villes* autant de fois que vous le souhaitez tant que vous n'entrez pas ***stop***.


- [main](#main)
- [data](#data)
- [__repr__](#repr)

## Les fonctions

### main

**Main** est une fonction qui prend un seule paramètre qui doit etre un tableau contenant uniquement des chaînes de caractères.

- Si le parametre de main est un tableau comprenant 2 chaine de caractere la fonction retourne un tableau qui comprend *(dans cette ordre)*: 
    - La ville de départ
    - La ville d'arrivé
    - Le nombre de km parcourue
    - Le temps pour réaliser l'itinéraire

- Si le parametre de main est un tableau comprenant plus de 2 chaine de caractere la fonction retourne un tableau de de tableau qui comprend *(dans cette ordre)*: 
    - des tableau qui sont la resultat de main avec seulement deux parametre.
    - KM total
    - Le nombre de km parcourue total
    - Le temps pour réaliser l'itinéraire total

### data

**Data** est une fonction qui prend un seule parametre un tableau contenant uniquement des chaînes de caractères. ( deux villes )

Elle va envoyer la rechercher des deux ville au site `https://www.bonnesroutes.com/widget/v1/html` et renvoie sous forme de tableau:
    - les Kms
    - Le temps en **h** 
    - Le temps en **m**

### Repr

C'est une fonction qui renvoie une chaine de caractere decrivant l'objet.
Elle est utilisée lors d'un ***print()*** de l'objet 

Exemple :

```
print(object)
```

### Pause

Elle prend en parametre des heures et des minutes et calcule si les minutes depasse 60, si oui, on rajoute une heure au heures.

Elle retourne une chaine de caractere contenant l'heure apres traitement et les minutes apres traitement.

### Tous

Tous est une fonction qui prend un parametre qui dois etre un tableau
et retourne un tableau

elle manipule le tableau pour ajouter tout sont contenue dans un second tableau et calcule tout les kilometres de chaque distance et le temps que cela met

### Demande

**Demande** ne prend pas de parametres.

Elle demande a l'utilisateur de rentrer des villes jusqu'a temps quelle y rentre **stop**.

Elle retourne un tableau de toutes les villes qu'il a rentré.