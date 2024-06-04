import os
import pymysql
from requetes_sql import *

dbConfig = {
    'driver': "MySQL",
    'db': 'rugby',
    'host': "localhost",
    'user': "admin",
    'passwd': "admin",
    'port': 3306
}

def dbConnect():
    """Connecte à la base de données et renvoie la connexion et le curseur."""
    db = pymysql.connect(
        host=dbConfig['host'],
        user=dbConfig['user'],
        passwd=dbConfig['passwd'],
        port=int(dbConfig['port']),
        db=dbConfig['db']
    )
    cursor = db.cursor()
    return db, cursor

def insertJoueur(nom: str, dateNaissance: str, poste: str, idEquipe: int, compo) -> None:
    """Insère un joueur dans la base de données."""
    req = insertRequestJou(nom.upper(), dateNaissance, poste, idEquipe, compo)
    execute(req)

def insertEquipe(equipe: str) -> None:
    """Insère une équipe dans la base de données."""
    try:
        req = insertRequestEqu(equipe)
        execute(req)
    except pymysql.err.ProgrammingError:
        print("Pas de guillemets svp.")

def insertMatchs(id_dom, id_ext, date, score) -> None:
    """Insère un match dans la base de données."""
    req = insertRequestMat(id_dom, id_ext, date, score)
    execute(req)

def insertStats(id_jou, id_mat, duree, essai, penalite, carton) -> None:
    """Insère des statistiques d'un joueur dans la base de données."""
    req = insertRequestStats(id_jou, id_mat, duree, essai, penalite, carton)
    execute(req)

def updateStats(duree, essai, penalites, cartons, id_jou, id_m) -> None:
    """Met à jour les statistiques d'un joueur dans la base de données."""
    req = updateStatsReq(duree, essai, penalites, cartons, id_jou, id_m)
    execute(req)

def insertPart(id_jou, id_mat) -> None:
    """Insère une participation d'un joueur à un match dans la base de données."""
    req = insertRequestPart(id_jou, id_mat)
    execute(req)

def execute(req: str):
    """Exécute une requête SQL et renvoie le résultat."""
    db, cursor = dbConnect()
    res = cursor.execute(req)
    if "select" in req.lower():
        res = cursor.fetchall()
    else:
        db.commit()
    return res

def getJoueur() -> list:
    """Renvoie une liste de tous les joueurs."""
    req = requetes["getAllJoueur"]
    return execute(req)

def getJoueurByNom(nom: str) -> list:
    """Renvoie une liste de joueurs par nom."""
    req = getByNom(nom)
    return execute(req)

def getJouParAge() -> list:
    """Renvoie une liste de joueurs par âge."""
    req = requetes["getJoueurParAge"]
    return execute(req)

def getJoueurParPoste(poste: str) -> list:
    """Renvoie une liste de joueurs par poste."""
    req = getByPoste(poste)
    return execute(req)

def getJouEqu(equ: str) -> list:
    """Renvoie une liste de joueurs par équipe."""
    req = getJouParEquipe(equ)
    return execute(req)

def getMatchs() -> list:
    """Renvoie une liste de tous les matchs."""
    req = requetes["getAllMatchs"]
    return execute(req)

def getCurrentMatchs(dom, ext) -> list:
    """Renvoie une liste des matchs récents."""
    req = getCurrentMatchsReq(dom, ext)
    return execute(req)

def getEquipe() -> list:
    """Renvoie une liste de toutes les équipes."""
    req = requetes["getAllEquipe"]
    return execute(req)

def getPoste() -> list:
    """Renvoie une liste de tous les postes."""
    req = requetes["getPoste"]
    return execute(req)

def getCompo(nom: str) -> list:
    """Renvoie la composition d'une équipe."""
    req = getCompoReq(nom)
    return execute(req)

def getStatsByJoueur(nom: str) -> list:
    """Renvoie les statistiques d'un joueur."""
    req = getStatsByJoueurReq(nom)
    return execute(req)

def getStatsByMatchs(id_m: int) -> list:
    """Renvoie les statistiques d'un match."""
    req = getStatsByMatchsReq(id_m)
    return execute(req)

def joueurToString(joueur: tuple) -> str:
    """Renvoie une représentation textuelle d'un joueur."""
    naissance = joueur[2].strftime("%d/%m/%Y")
    req = id2equipe(joueur[4])
    return f"{joueur[0]} : {joueur[1]} | Né le {naissance} | Poste : {joueur[3]} | Equipe : {(execute(req))[0][0]}"

def jouAgeToString(joueur: tuple) -> str:
    """Renvoie une représentation textuelle d'un joueur par âge."""
    naissance = joueur[2].strftime("%d/%m/%Y")
    return f"{joueur[1]} né le {naissance}"

def nomJouToString(nom: tuple) -> str:
    """Renvoie une représentation textuelle d'un joueur par nom."""
    req = id2equipe(nom[4])
    return f"{nom[1]} joue dans l'équipe {(execute(req))[0][0]}"

def jouPosteToString(joueur: tuple) -> str:
    """Renvoie une représentation textuelle d'un joueur par poste."""
    return f"{joueur[1]} joue {joueur[3]}"

def equipeToString(equ: tuple) -> str:
    """Renvoie une représentation textuelle d'une équipe."""
    return f"{equ[1]}"

def jouEquToString(joueur: tuple) -> str:
    """Renvoie une représentation textuelle d'un joueur par équipe."""
    return f"{joueur[0]}"

def matchsToString(mat: tuple) -> str:
    """Renvoie une représentation textuelle d'un match."""
    date = mat[3].strftime("%d/%m/%Y")
    req1 = id2equipe(mat[1])
    req2 = id2equipe(mat[2])
    return f"{mat[0]} : {(execute(req1))[0][0]} {mat[4]} {(execute(req2))[0][0]} | {date}"

def dbJouToString() -> str:
    """Renvoie une représentation textuelle de tous les joueurs."""
    s = []
    for jou in getJoueur():
        s.append(joueurToString(jou))
    return s

def dbNomJouToString(nom: str) -> str:
    """Renvoie une représentation textuelle de joueurs par nom."""
    s = []
    for n in getJoueurByNom(nom):
        s.append(nomJouToString(n))
    return s

def dbJouEquToString(equipe: str) -> str:
    """Renvoie une représentation textuelle de joueurs par équipe."""
    s = []
    for equ in getJouEqu(equipe):
        s.append(jouEquToString(equ))
    return s

def dbJouAgeToString() -> str:
    """Renvoie une représentation textuelle de joueurs par âge."""
    s = []
    for age in getJouParAge():
        s.append(jouAgeToString(age))
    return s

def dbJouPosteToString(poste: str) -> str:
    """Renvoie une représentation textuelle de joueurs par poste."""
    s = []
    for postes in getJoueurParPoste(poste):
        s.append(jouPosteToString(postes))
    return s

def dbEquToString() -> str:
    """Renvoie une représentation textuelle de toutes les équipes."""
    s = []
    for equ in getEquipe():
        s.append(equipeToString(equ))
    return s

def dbMatToString() -> str:
    """Renvoie une représentation textuelle de tous les matchs."""
    s = []
    for mat in getMatchs():
        s.append(matchsToString(mat))
    return s

def jouToCSV(joueur: tuple) -> str:
    """Renvoie une représentation CSV d'un joueur."""
    naissance = joueur[2].strftime("%d/%m/%Y")
    return f"{joueur[0]};{joueur[1]};{naissance};{joueur[3]};{joueur[4]};"

def equToCSV(equ: tuple) -> str:
    """Renvoie une représentation CSV d'une équipe."""
    return f"{equ[0]};{equ[1]};"

def matToCSV(mat: tuple) -> str:
    """Renvoie une représentation CSV d'un match."""
    date = mat[3].strftime("%d/%m/%Y")
    return f"{mat[0]};{mat[1]};{mat[2]};{date};{mat[4]};"

def dbJouToFile() -> str:
    """Renvoie le contenu de la base sous forme de chaîne de caractères au format CSV."""
    s = ''
    for jou in getJoueur():
        s = s + jouToCSV(jou) + '\n'
    return s

def dbEquToFile() -> str:
    """Renvoie le contenu de la base sous forme de chaîne de caractères au format CSV."""
    s = ''
    for equ in getEquipe():
        s = s + equToCSV(equ) + '\n'
    return s

def dbMatToFile() -> str:
    """Renvoie le contenu de la base sous forme de chaîne de caractères au format CSV."""
    s = ''
    for mat in getMatchs():
        s = s + matToCSV(mat) + '\n'
    return s

def deleteJoueur(nom: str) -> None:
    """Supprime un joueur de la base de données."""
    n = nom.upper()
    reqVerif = getByNom(n)
    if len(execute(reqVerif)) == 0:
        raise ValueError("Le joueur n'existe pas.")
    req = deleteRequestJou(n)
    execute(req)

def deleteEquipe(nom: str) -> None:
    """Supprime une équipe de la base de données."""
    n = nom.capitalize()
    reqVerif = getByNomEqu(n)
    if len(execute(reqVerif)) == 0:
        raise ValueError("L'équipe n'existe pas.")
    try:
        req1 = deleteRequestJouEqu(n)
        execute(req1)
        req2 = deleteRequestEqu(n)
        execute(req2)
    except pymysql.err.ProgrammingError:
        print("Pas de guillemets svp.")

def deleteMatchs(num: int) -> None:
    """Supprime un match de la base de données."""
    req = deleteRequestMat(num)
    execute(req)

def deleteBase() -> None:
    """Supprime la base de données."""
    req = requetes["drop"]
    execute(req)

def jouToTextFile(path="joueurs.txt") -> None:
    """Écrit le contenu des joueurs dans un fichier texte."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(dbJouToFile())

def equToTextFile(path="equipe.txt") -> None:
    """Écrit le contenu des équipes dans un fichier texte."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(dbEquToFile())

def matToTextFile(path="matchs.txt") -> None:
    """Écrit le contenu des matchs dans un fichier texte."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(dbMatToFile())
