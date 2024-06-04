import cherrypy
import os
from mako.template import Template
from mako.lookup import TemplateLookup
from requetes_sql import *
from fonctionnalite_CRUD import *
from createBase import *

# Initialisation de TemplateLookup pour Mako
mylookup = TemplateLookup(directories=['static/templates'], module_directory='static/tmp/mako_modules')

class RugbyApp:
    def __init__(self):
        """Initialise la base et demande si on veut la créer si elle n'existe pas"""
        initBase()

    # Méthodes pour obtenir les données
    def get_equipe(self):
        """Donne les équipes sous forme d'un tuple"""
        return getEquipe()

    def getJoueur(self):
        """Donne les joueurs sous forme d'un tuple"""
        return getJoueur()

    def get_joueurs_par_equipe(self, equipe):
        """Donne les joueurs d'une équipe sous forme d'un tuple avec l'équipe en paramètre"""
        return getJouEqu(equipe)
    
    def get_joueur_par_poste(self, poste):
        """Donne les joueurs par poste sous forme d'un tuple avec le poste en paramètre"""
        return getJoueurParPoste(poste)
    
    def get_joueur_par_age(self):
        """Donne les joueurs par âge sous forme d'un tuple"""
        return getJouParAge()
    
    def get_joueur_par_nom(self, nom):
        """Donne les joueurs par nom sous forme d'un tuple avec nom et prénom en paramètre"""
        return getJoueurByNom(nom)
    
    def get_matchs(self):
        """Donne les matchs sous forme d'un tuple"""
        return getMatchs()
    
    def get_compo(self, nom):
        """Donne la composition des équipes avec comme paramètre le nom des joueurs"""
        return getCompo(nom)
    
    def get_poste(self):
        """Donne les postes"""
        return getPoste()
    
    def get_stats(self, nom):
        """Donne les stats d'un joueur"""
        return getStatsByJoueur(nom)
    
    def get_current_match_id(self, dom, ext):
        """Donne le match le plus récent"""
        return getCurrentMatchs(dom, ext)
    
    # Méthodes pour insérer des données
    def insert_stats(self, id_jou, id_mat, duree, essai, penalite, carton):
        """Permet d'insérer des stats sur un joueur"""
        return insertStats(id_jou, id_mat, duree, essai, penalite, carton)
    
    def insertEquipe(self, equipe):
        """Permet d'insérer une équipe"""
        insertEquipe(equipe)
    
    def insertJoueur(self, nom, dateNaissance, poste, idEquipe):
        """Permet d'insérer un joueur"""
        insertJoueur(nom, dateNaissance, poste, idEquipe)
    
    def insertmatchs(self, dom, ext, date, result):
        """Permet d'insérer un match"""
        insertMatchs(dom, ext, date, result)
    
    # Méthodes pour supprimer des données
    def deleteequipe(self, equipe):
        """Suppression d'une équipe dans la base de données"""
        deleteEquipe(equipe)
    
    def deleteJoueur(self, nom):
        """Suppression d'un joueur dans la base de données"""
        deleteJoueur(nom)
    
    def deleteMatch(self, match_id):
        """Suppression d'un match dans la base de données"""
        deleteMatchs(match_id)
    
    # Méthodes exposées via l'interface web
    @cherrypy.expose
    def index(self):
        """Affiche la page d'accueil avec la composition des équipes et les événements"""
        clermont_compo = self.get_compo("Clermont")
        toulouse_compo = self.get_compo("Toulouse")
        events = [
            {"time": "5", "event": "Try", "team": "Clermont", "player": "GEORGE MOALA", "ID_matchs": 38},
            {"time": "11", "event": "Penalty", "team": "Toulouse", "player": " THOMAS RAMOS", "ID_matchs": 38},
            {"time": "19", "event": "Try", "team": "Toulouse", "player": "ANTOINE DUPONT", "ID_matchs": 38},
            {"time": "27", "event": "Yellow Card", "team": "Clermont", "player": "FRITZ LEE", "ID_matchs": 38},
            {"time": "35", "event": "Try", "team": "Clermont", "player": "DAMIAN PENAUD", "ID_matchs": 38},
            {"time": "39", "event": "Penalty", "team": "Toulouse", "player": "THOMAS RAMOS", "ID_matchs": 38},
            {"time": "42", "event": "Try", "team": "Toulouse", "player": "CYRIL BAILLE", "ID_matchs": 38},
            {"time": "54", "event": "Penalty", "team": "Clermont", "player": "CAMILLE LOPEZ", "ID_matchs": 38},
            {"time": "62", "event": "Try", "team": "Clermont", "player": "MORGAN PARRA", "ID_matchs": 38},
            {"time": "68", "event": "Penalty", "team": "Toulouse", "player": "THOMAS RAMOS", "ID_matchs": 38},
            {"time": "75", "event": "Yellow Card", "team": "Toulouse", "player": "FRANCOIS CROS", "ID_matchs": 38},
            {"time": "80", "event": "Try", "team": "Toulouse", "player": "ROMAIN NTAMACK", "ID_matchs": 38},
        ]
        poste = self.get_poste()

        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render(clermont_compo=clermont_compo, toulouse_compo=toulouse_compo, events=events, poste=poste)

    @cherrypy.expose
    def equipe(self):
        """Affiche la page des équipes"""
        equipes = self.get_equipe()
        poste = self.get_poste()
        mytemplate = mylookup.get_template("equipe.html")
        return mytemplate.render(equipes=equipes, poste=poste)

    @cherrypy.expose
    def joueur_par_equipe(self, equipe):
        """Affiche les joueurs d'une équipe spécifique"""
        joueurs = self.get_joueurs_par_equipe(equipe)
        poste = self.get_poste()
        mytemplate = mylookup.get_template("joueursParEquipe.html")
        return mytemplate.render(equipe=equipe, joueurs=joueurs, poste=poste)

    @cherrypy.expose
    def insert_equipe(self, equipe):
        """Insertion d'une équipe via le formulaire"""
        try:
            self.insertEquipe(equipe)
        except ValueError:
            return "Erreur lors de l'insertion de l'équipe."
        raise cherrypy.HTTPRedirect("/equipe")
    
    @cherrypy.expose
    def insert_joueur(self, nom, dateNaissance, poste, idEquipe):
        """Insertion d'un joueur via le formulaire"""
        try:
            self.insertJoueur(nom, dateNaissance, poste, idEquipe)
        except ValueError:
            return "Erreur lors de l'insertion du joueur."
        raise cherrypy.HTTPRedirect("/joueur")
    
    @cherrypy.expose
    def delete_equipe(self, equipe):
        """Suppression d'une équipe via le formulaire"""
        try:
            self.deleteequipe(equipe)
        except Exception:
            return "Erreur lors de la suppression de l'équipe."
        raise cherrypy.HTTPRedirect("/equipe")

    @cherrypy.expose
    def joueur(self):
        """Affiche la page des joueurs"""
        poste = self.get_poste()
        equipes = self.get_equipe()
        mytemplate = mylookup.get_template("joueur.html")
        return mytemplate.render(poste=poste, equipes=equipes)

    @cherrypy.expose
    def joueur_par_nom(self, nom):
        """Affiche les joueurs par nom"""
        joueurs = self.get_joueur_par_nom(nom)
        poste = self.get_poste()
        mytemplate = mylookup.get_template("joueurParNom.html")
        return mytemplate.render(joueurs=joueurs, nom=nom, poste=poste)
    
    @cherrypy.expose
    def get_joueur(self):
        """Affiche tous les joueurs"""
        joueurs = self.getJoueur()
        poste = self.get_poste()
        mytemplate = mylookup.get_template("AllJoueur.html")
        return mytemplate.render(joueurs=joueurs, poste=poste)
    
    @cherrypy.expose
    def joueur_par_poste(self, poste):
        """Affiche les joueurs par poste"""
        joueurs = self.get_joueur_par_poste(poste)
        mytemplate = mylookup.get_template("joueurParPoste.html")
        return mytemplate.render(joueurs=joueurs, poste=poste)
    
    @cherrypy.expose
    def joueur_par_age(self):
        """Affiche les joueurs par âge"""
        joueurs = self.get_joueur_par_age()
        poste = self.get_poste()
        mytemplate = mylookup.get_template("joueurParAge.html")
        return mytemplate.render(joueurs=joueurs, poste=poste)

    @cherrypy.expose
    def delete_joueur(self, nom):
        """Suppression d'un joueur via le formulaire"""
        try:
            self.deleteJoueur(nom)
        except ValueError:
            return "Erreur lors de la suppression du joueur."
        raise cherrypy.HTTPRedirect("/joueur")

    @cherrypy.expose
    def matchs(self):
        """Affiche la page des matchs"""
        equipe = self.get_equipe()
        matchs = self.get_matchs()
        poste = self.get_poste()
        mytemplate = mylookup.get_template("matchs.html")
        return mytemplate.render(matchs=matchs, equipe=equipe, poste=poste)
    
    @cherrypy.expose
    def insert_matchs(self, dom, ext, date, result):
        """Insertion d'un match via le formulaire"""
        try:
            self.insertmatchs(dom, ext, date, result)
        except ValueError:
            return "Erreur lors de l'insertion du match."
        raise cherrypy.HTTPRedirect("/matchs")
    
    @cherrypy.expose
    def delete_match(self, match_id):
        """Suppression d'un match via le formulaire"""
        try:
            self.deleteMatch(match_id)
        except ValueError:
            return "Erreur lors de la suppression du match."
        raise cherrypy.HTTPRedirect("/matchs")

if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print(f"La racine du site est :\n\t{rootPath}\n\tcontient : {os.listdir()}")
    cherrypy.quickstart(RugbyApp(), '/', 'config.txt')
