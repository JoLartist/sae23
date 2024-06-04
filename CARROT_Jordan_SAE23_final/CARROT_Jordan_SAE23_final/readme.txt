Rugby Application - README
==========================

1. Procédure pour lancer l'application
--------------------------------------
1. Assurez-vous d'avoir Python installé sur votre machine.
2. Exécuter "python3 RugbyApp.py" dans le shell et le site est lancé ! 
(un fichier initBase() vous proposera de créer la base).

--------------------------------------

L'application est divisée en deux parties: l'admin et la publique.

Partie Admin:

Ajout et suppression d'équipes.
Ajout et suppression de joueurs.
Ajout et suppression de matchs.
A la fin de chaque page, un bouton administrateur a été ajouter afin d'afficher les formualaires
permettant ces opérations.

--------------------------------------

Partie Publique:

Affichage des équipes et des joueurs par équipe.
Affichage des joueurs par poste, âge et nom.
Affichage des compositions des équipes et des événements des matchs sur la page d'accueil.
Affichage des matchs et de leurs résultats.

--------------------------------------

Depuis l'étape 2, aucunes modifications n'ont été apportées.

--------------------------------------

Fonctionnalités prévus :

Events du match intérer dans la table statistiques pour chaque joueur 

--------------------------------------

L'archive contient les fichiers et répertoires suivants:
--------------------------------------
    static: Répertoire contenant les fichiers statiques (CSS, images, JavaScript).
--------------------------------------
    css: Feuilles de style utilisées dans l'application.
--------------------------------------
    fonts: Polices de caractères utilisées dans l'application.
--------------------------------------
    images: Images utilisées dans l'application.
--------------------------------------
    js: Scripts JavaScript utilisés dans l'application.
--------------------------------------
    templates: Templates Mako pour rendre les pages HTML.
--------------------------------------
    tmp/mako_modules: Fichiers temporaires générés par Mako.
--------------------------------------
    calendrierTop14_2023.csv: Fichier CSV contenant les données des matchs du Top 14 pour 2023.
--------------------------------------
    app.py: Fichier principal de l'application.
--------------------------------------
    config.txt: Fichier de configuration pour CherryPy.
--------------------------------------
    requetes_sql.py: Fichier contenant les requêtes SQL pour interagir avec la base de données.
--------------------------------------
    fonctionnalité_CRUD.py: Fichier contenant les fonctions CRUD pour gérer les données.
--------------------------------------
    createBase.py: Script pour initialiser et créer la base de données.

--------------------------------------

En cas d'impossibilté de lancer le site, le dump de la base est disponible ainsi que "createBaseSQL.py" permettant la création de la base et l'import des données depuis un CSV.