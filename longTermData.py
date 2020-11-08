import sqlite3

conn = sqlite3.connect("longTermData.db")
cur = conn.cursor()
def createPlayer(name):
    sqlite_insert_with_param = """INSERT INTO PLAYER
                              (Name, Level, Cash, GamesPlayed) 
                              VALUES (?, ?, ?, ?);"""
    data_tuple = (name, 0, 0, 0)
    cur.execute(sqlite_insert_with_param, data_tuple)
    print("inserted player")

def createPlayerPlanes(owner, planeName):
    sqlite_insert_with_param = """INSERT INTO PLAYERPLANES
                              (Owner, Name, Health, MoveSpeed) 
                              VALUES (?, ?, ?, ?);"""
    data_tuple = (owner, planeName, 0, 0)
    cur.execute(sqlite_insert_with_param, data_tuple)
    print("inserted plane")

def createPlayerPlaneUpgrades(owner, upgrade, planeName):
    sqlite_insert_with_param = """INSERT INTO PLAYERPLANEUPGRADES
                              (Owner, Upgrade, Plane) 
                              VALUES (?, ?, ?);"""
    data_tuple = (owner, upgrade, planeName)
    cur.execute(sqlite_insert_with_param, data_tuple)
    print("inserted player plane upgrade new")

def getPlayers():
    cur.execute("""SELECT * FROM PLAYER""")
    before = cur.fetchall()
    for i in before:
        print(i)

def getPlayerPlanes(name):
    cur.execute("Select Name FROM PLAYERPLANES WHERE Owner LIKE '%'||?||'%';", (name, ))
    before = cur.fetchall()
    return before

def getPlayerPlanesUpgrades(name, plane):
    cur.execute("Select Upgrade FROM PLAYERPLANEUPGRADES WHERE Owner LIKE '%'||?||'%' AND Plane LIKE '%'||?||'%' ;", (name,plane ))
    before = cur.fetchall()
    return before



def createPlayerTable():
    table = cur.execute("""
        CREATE TABLE PLAYER(
            Name CHAR(20),
            Level INT,
            Cash INT,
            GamesPlayed INT
        )
        """
                        )
    print("Successfully created player")

def createPlaneTable():
    table = cur.execute("""
        CREATE TABLE PLAYERPLANES(
            Owner CHAR(20),
            Name CHAR(20),
            Health INT,
            MoveSpeed INT
        )
        """
                        )
    print("Successfully created player plane")

def createPlaneUpgradeTable():
    table = cur.execute("""
        CREATE TABLE PLAYERPLANEUPGRADES(
            Owner CHAR(20),
            upgrade CHAR(20),
            plane CHAR(20)
        )
        """
                        )
    print("Successfully created player plane upgrade")


def closeConnection():
    conn.commit()
    conn.close()
