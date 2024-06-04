#Les fonctions suivantes permettent de faire des requêtes SQL avec valeurs variables

requetes = {
    "drop" : "DROP DATABASE IF EXISTS rugby",
    "createBase" : "CREATE DATABASE IF NOT EXISTS rugby DEFAULT CHARACTER SET utf8",
    "use" : "USE rugby",
    "createTableEquipe" : "CREATE TABLE Equipe (ID INT AUTO_INCREMENT PRIMARY KEY, Nom_equipe VARCHAR(255))ENGINE=InnoDB;",
    "createTableJoueur" : "CREATE TABLE Joueur (ID INTEGER AUTO_INCREMENT PRIMARY KEY, Nom VARCHAR(255), Date_naissance DATE, Poste_prefere VARCHAR(255), ID_equipe INT, in_composition BOOLEAN DEFAULT FALSE, FOREIGN KEY (ID_equipe) REFERENCES Equipe(ID))ENGINE=InnoDB;",
    "createTableMatchs" : "CREATE TABLE Matchs (ID INT AUTO_INCREMENT PRIMARY KEY, ID_equipe_domicile INT, ID_equipe_exterieur INT, Date_matchs DATE, Resultat_matchs VARCHAR(255), FOREIGN KEY (ID_equipe_domicile) REFERENCES Equipe(ID), FOREIGN KEY (ID_equipe_exterieur) REFERENCES Equipe(ID))ENGINE=InnoDB;",
    "createTableStats" : "CREATE TABLE Statistiques (ID INT AUTO_INCREMENT PRIMARY KEY, ID_joueur INT, ID_matchs INT, Duree_jeu INT, Nombre_essais INT, Nombre_penalites INT, Nombre_cartons INT,FOREIGN KEY (ID_joueur) REFERENCES Joueur(ID), FOREIGN KEY (ID_matchs) REFERENCES Matchs(ID))ENGINE=InnoDB;",
    "createTableParticiper" : "CREATE TABLE Participer (ID_joueur INT, ID_matchs INT,FOREIGN KEY (ID_joueur) REFERENCES Joueur(ID), FOREIGN KEY (ID_matchs) REFERENCES Matchs(ID))ENGINE=InnoDB;",
    "getAllJoueur" : "select * from Joueur order by ID;",
    "getAllMatchs" : "select * from Matchs order by Date_matchs;",
    "getAllEquipe" : "select * from Equipe order by ID;",
    "getAllStats" : "select * from Statistiques;",
    "updateStats" : "update Statistiques SET Duree_jeu = {}, Nombre_essais = {}, Nombre_penalites = {}, Nombre_cartons = {} WHERE ID_joueur = {} AND ID_matchs = {};",
    "getStatsByJoueur" : "select * from Statistiques JOIN Joueur ON Statistiques.ID_joueur = Joueur.ID WHERE Nom='{};",
    "getStatsByMatchs" : "select * from Statistiques JOIN matchs ON Statistiques.ID_joueur = matchs.ID_joueur WHERE matchs.ID = {};",
    "getCurrentMatchs" : "select ID_matchs from matchs WHERE ID_equipe_domicile = {} OR ID_equipe_exterieur = {} ORDER BY Date DESC LIMIT 1;",
    "getJoueurParAge" : "select * from Joueur order by Date_naissance;",
    "getJoueurParPoste" : "select * from Joueur where Poste_prefere='{}';",
    "getJoueurParEquipe" : "select * FROM Joueur JOIN Equipe ON Joueur.ID_equipe = Equipe.ID WHERE Nom_equipe = '{}';",
    "getCompo" : "select Nom, Poste_prefere FROM Joueur JOIN Equipe ON Joueur.ID_equipe = Equipe.ID WHERE Nom_equipe = '{}' AND in_composition = 1;",
    "getById" : "select * from {} where ID = {};",
    "getByNom" : "select * from Joueur where Nom = '{}' ;",
    "getPoste" : "select DISTINCT(Poste_prefere) from Joueur;",
    "getByNomEqu" : "select * from Equipe where Nom_equipe = '{}';",
    "insertJou" : "insert into Joueur(Nom,Date_naissance,Poste_prefere,ID_equipe,in_composition) values ('{}','{}','{}','{}',{});",
    "insertEqu" : "insert into Equipe(Nom_equipe) values('{}')",
    "insertMat" : "insert into Matchs(ID_equipe_domicile, ID_equipe_exterieur, Date_matchs, Resultat_matchs) values ('{}', '{}', '{}', '{}');",
    "insertPart" : "insert into Participer(ID_joueur, ID_matchs) Values ({}, {});",
    "insertStats" : "insert into statistiques(ID_joueur, ID_matchs, Duree_jeu, Nombre_essais, Nombre_penalites, Nombre_cartons) values({}, {}, {}, {}, {}, {});",
    "deleteJou" : "delete from Joueur where Nom = '{}';",
    "deleteEqu" : "delete from Equipe where Nom_equipe = '{}';",
    "deleteMat" : "delete from Matchs where ID = {};",
    "deleteByNum" : "delete from {} where ID = {};",
    "deleteJoueurFromEqu" : "DELETE Joueur FROM Joueur INNER JOIN Equipe ON Joueur.ID_equipe = Equipe.ID WHERE Nom_equipe = '{}';",
    "id2equipe" : "select DISTINCT(Nom_equipe) FROM Equipe JOIN Joueur ON Equipe.ID = Joueur.ID_equipe WHERE ID_equipe = {};",
    "equipe2id" : "select DISTINCT(Joueur.ID_equipe) FROM Joueur JOIN equipe ON Joueur.ID_equipe = Equipe.ID WHERE Nom_equipe = '{}';" }

def insertRequestJou(nom,age,poste,id_equ, compo) :
    s = requetes["insertJou"].format(nom,age,poste,id_equ, compo)
    return s

def insertRequestEqu(equipe) :
    s = requetes["insertEqu"].format(equipe)
    return s

def insertRequestMat(id_dom, id_ext, date, score) :
    s = requetes["insertMat"].format(id_dom, id_ext, date, score)
    return s

def insertRequestPart(id_jou, id_mat) :
    s = requetes["insertPart"].format(id_jou, id_mat)
    return s

def insertRequestStats(id_jou, id_mat, duree, essai, penalite, carton) :
    s = requetes["insertStats"].format(id_jou, id_mat, duree, essai, penalite, carton)
    return s

def updateStatsReq(duree, essai, penalites, cartons, id_jou, id_m) :
    s = requetes["updateStats"].format(duree,essai,penalites, cartons, id_jou, id_m)
    return s

def deleteRequestJou(nom) :
    s = requetes["deleteJou"].format(nom.upper())
    return s

def deleteRequestEqu(nom) :
    s = requetes["deleteEqu"].format(nom.capitalize())
    return s

def deleteRequestJouEqu(nom) :
    s = requetes["deleteJoueurFromEqu"].format(nom)
    return s

def deleteRequestMat(num) :
    s = requetes["deleteMat"].format(num)
    return s

def deleteByNum(table, num) :
    s = requetes["deleteByNum"].format(table, num)
    return s

def getByNum(table, num) :
    s = requetes["getById"].format(table.capitalize(), num)
    return s

def getCompoReq(nom) : 
    s = requetes["getCompo"].format(nom)
    return s

def getStatsByJoueurReq(nom) :
    s = requetes["getStatsByJoueur"].format(nom)
    return s

def getStatsByMatchsReq(id_m) :
    s = requetes["getStatsByMatchs"].format(id_m)
    return s

def getByNom(nom) :
    s = requetes["getByNom"].format(nom.upper())
    return s

def getByNomEqu(nom) :
    s = requetes["getByNomEqu"].format(nom)
    return s

def getByMatchs(num) :
    s = requetes["getByIDMatchs"].format(num)
    return s

def getCurrentMatchsReq(dom, ext):
    s = requetes["getCurrentMatchs"].format(dom, ext)
    return s

def getByPoste(poste) :
    s = requetes["getJoueurParPoste"].format(poste)
    return s

def getJouParEquipe(nom) :
    s = requetes["getJoueurParEquipe"].format(nom)
    return s

def id2equipe(id_equ:int) :
    s = requetes["id2equipe"].format(id_equ)
    return s

def equipe2id(nom) :
    s = requetes["equipe2id"].format(nom)
    return s
