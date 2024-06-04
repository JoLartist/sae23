from requetes_sql import requetes, insertRequestJou, insertRequestEqu, insertRequestMat, deleteRequestJou, deleteRequestEqu, deleteByNum, getByNum, getByNom, getByMatchs, getByNomEqu
from fonctionnalite_CRUD import insertEquipe, insertJoueur, insertMatchs

dbConfig = {
        'driver' : "MySQL",
        'db' : 'rugby',
        'host' : "localhost",
        'user' : "admin",
        'passwd' : "admin",
        'port' : 3306
    }

def ParamsConnexion() -> None:
    # ne gère que MYSQL
    # récup des paramètres dans le fichier de conf
    # paramètres MYSQL, valeurs par défaut
    # le port sera stocké comme une chaîne
    try :
        with open("config.txt", 'r', encoding="utf-8") as f :
            for ligne in f :
                if ligne[0] == '#' or ligne[0] == '[' or len(ligne)<3 :
                    continue
                champs = ligne.split(':')
                dbConfig[champs[0].strip()] = champs[1].strip().strip('"')
    except FileNotFoundError as e :
        print("'config.txt' absent, utilisation des valeurs par défaut")

def dbConnect():
    # récup des paramètres dans le fichier de conf
    import pymysql
    db = pymysql.connect(host = dbConfig['host'], user=dbConfig['user'], passwd=dbConfig['passwd'], port=int(dbConfig['port']), db = dbConfig['db'])
    cursor=db.cursor()
    return (db,cursor)

def createBaseSQL() -> None :
    """Crée la base"""
    import pymysql
    db = pymysql.connect(host = dbConfig['host'], user=dbConfig['user'], passwd=dbConfig['passwd'], port=int(dbConfig['port']))
    cursor = db.cursor()
    cursor.execute(requetes["drop"])
    cursor.execute(requetes["createBase"])
    cursor.execute(requetes["use"])
    cursor.execute(requetes["createTableEquipe"])
    cursor.execute(requetes["createTableJoueur"])
    cursor.execute(requetes["createTableMatchs"])
    cursor.execute(requetes["createTableStats"])
    cursor.execute(requetes["createTableParticiper"])
    print("Base crée")

def initBase() -> None :
    """Vérifie si la base donnée est bien présente sinon demande si on veut la créée"""
    ParamsConnexion()
    print(dbConfig['driver'].upper())
    match dbConfig['driver'].upper() :
        case "MYSQL" :
            try :
                import pymysql
                db = pymysql.connect(host=dbConfig['host'], user=dbConfig['user'], passwd=dbConfig['passwd'], port=int(dbConfig['port']), db=dbConfig['db'])
                cursor = db.cursor()
                print("Base initialisé")
            except pymysql.err.OperationalError as e :
                print("hello")
                print(e)
                if '1044' in str(e) :
                    print(f"Vérifiez les paramètres de connexion à la base {dbConfig['db']}")
                elif '1049' in str(e) :
                    choix = input("Base inexistante, voulez-vous la créer ?")
                    if choix.upper() in ('O','OUI','Y','YES') :
                        createBaseSQL()
                        loadEquJouFromCSVFile("JoueursTop14.csv")
                        loadResultFromCSVFile("calendrierTop14_2023.csv")
                    else :
                        raise e
        case _ :
            print(f"SGBDR {dbConfig['driver'].upper()} non géré")
            raise ValueError
 #Cette fonction importe les équipes et les joueurs depuis un fichier CSV dans une BD

#Les fonctions suivantes vont convertir des dates ISO en date normal et inversement
def iso2str(date:str)->str :
    """aaaa-mm-jj --> jj/mm/aaaa/"""
    d = date.split('-')
    s = d[2]+"/"+d[1]+"/"+d[0]
    return s

def str2iso(date:str) -> str :
    """jj/mm/aaaa --> aaaa-mm-jj"""
    d = date.split('/')
    s = d[2]+"-"+d[1]+"-"+d[0]
    return s



def loadEquJouFromCSVFile(path: str) -> None:
    """ Permet de charger une liste de joueur et d'équipe à partir d'un fichier texte "CSV" """
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignes = csv.reader(csvFile,delimiter=';')
        next (lignes)
        for champs in lignes :
            equipe = champs[8]
            if champs[8] == '' :
                continue
            insertEquipe(equipe)
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignes = csv.reader(csvFile,delimiter=';')
        next (lignes)
        for champs in lignes : 
            nom = champs[1]
            poste = champs[2]
            date = str2iso(champs[4])
            id_equ = champs[7]
            compo = champs[9]
            insertJoueur(nom,date,poste,id_equ, compo)
#Cette fonction prends des résulatats de matchs dans un fichiers csv et les importes dans la BD
def loadResultFromCSVFile(path :str) :
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignes = csv.reader(csvFile,delimiter=';')
        next (lignes)
        for champs in lignes :
            id_dom = champs[1]
            id_ext = champs[2]
            date = str2iso(champs[0])
            score = champs[3]
            insertMatchs(id_dom, id_ext, date, score)
        print("Equipes, joueurs, matchs mis dans la base de données")
            


if __name__ == '__main__' :
    createBaseSQL()
    loadEquJouFromCSVFile("JoueursTop14.csv")
    loadResultFromCSVFile("calendrierTop14_2023.csv")












    
