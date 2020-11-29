import sqlite3

conn = sqlite3.connect("longTermData.db")
cur = conn.cursor()

def dropLevel():
    cur.execute("DROP TABLE LEVELS")
def dropUpgrades():
    deleteUpgrades("Peyton")
    cur.execute("DROP TABLE PLAYERPLANEUPGRADES")

def deletePlayer():
    cur.execute("DELETE FROM PLAYER;")
    print("Deleted Players")

def deleteUpgrades(name):
    cur.execute("DELETE FROM PLAYERPLANEUPGRADES WHERE Owner LIKE '%'||?||'%';", (name, ))
    print("Deleted Upgrades")

def deletePlanes(name):
    cur.execute("DELETE FROM PLAYERPLANES WHERE Owner LIKE '%'||?||'%';", (name, ))
    print("Deleted planes")
def deleteLevels(name):
    cur.execute("DELETE FROM LEVELS WHERE Owner LIKE '%'||?||'%';", (name, ))
    print("Deleted planes")

def updatePlayerCash(cash, name):
    cur.execute("UPDATE PLAYER SET Cash =  (''||?||'' + (SELECT Cash FROM PLAYER WHERE Name LIKE '%'||?||'%'))  WHERE Name LIKE '%'||?||'%';", (cash,name, name ))

def updatePlayerGamesPlayed(name):
    cur.execute("UPDATE PLAYER SET GamesPlayed =  (1 + (SELECT Cash FROM PLAYER WHERE Name LIKE '%'||?||'%'))  WHERE Name LIKE '%'||?||'%';", (name, name ))

def updatePlayerLevel(level, name):
    cur.execute("UPDATE PLAYER SET Level =  (''||?||'' )  WHERE Name LIKE '%'||?||'%';", (level, name ))

def updateLevelComplete(level, starsEarned, score, name):
    cur.execute("UPDATE LEVELS SET Completed =  True WHERE Owner LIKE '%'||?||'%' AND level = ''||?||'';", (name, level))
    PrevStarsEarned = getLevelStarsEarned(name, level)[0][0]
    if(starsEarned > PrevStarsEarned):
        cur.execute("UPDATE LEVELS SET MaxScore =  (''||?||'' ) WHERE Owner LIKE '%'||?||'%' AND level = ''||?||'';", (score, name, level ))
        cur.execute("UPDATE LEVELS SET StarsEarned = (''||?||'' ) WHERE Owner LIKE '%'||?||'%' AND level = ''||?||'';", (starsEarned, name, level ))
        updatePlayerCash(starsEarned-PrevStarsEarned, name)
            # Owner CHAR(20),
            #  StarsEarned INT,
            # MaxScore INT,
            # Level INT,
            # Completed BOOLEAN
    

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

def createPlayerPlaneUpgrades(owner, upgrade, planeName, icon):
    sqlite_insert_with_param = """INSERT INTO PLAYERPLANEUPGRADES
                              (Owner, Upgrade, Plane, Icon) 
                              VALUES (?, ?, ?, ?);"""
    data_tuple = (owner, upgrade, planeName, icon)
    cur.execute(sqlite_insert_with_param, data_tuple)
    updatePlayerCash(-3, owner)
    print("inserted player plane upgrade new")

def createLevel(owner, level):
    sqlite_insert_with_param = """INSERT INTO LEVELS
                              (Owner, StarsEarned, MaxScore, Level, Completed) 
                              VALUES (?, ?, ?,  ?, ?);"""
    data_tuple = (owner, 0, 0, level, False)
    cur.execute(sqlite_insert_with_param, data_tuple)
    print("inserted new level")


def getPlayers():
    cur.execute("""SELECT * FROM PLAYER""")
    before = cur.fetchall()
    for i in before:
        print(i)

def printLevels():
    cur.execute("""SELECT * FROM LEVELS""")
    before = cur.fetchall()
    for i in before:
        print(i)

def printPlayerPlanes():
    cur.execute("""SELECT * FROM PLAYERPLANES""")
    before = cur.fetchall()
    for i in before:
        print(i)

def getPlayerCash(name):
    cur.execute("SELECT Cash FROM PLAYER WHERE NAME LIKE '%'||?||'%';", (name, ))
    before = cur.fetchall()
    return before        

def getLevels(name):
    cur.execute("SELECT * FROM LEVELS WHERE Owner LIKE '%'||?||'%';", (name, ))
    before = cur.fetchall()
    return before

def getLevelMaxScore(name, level):
    cur.execute("SELECT MaxScore FROM LEVELS WHERE Owner LIKE '%'||?||'%' AND Level = ''||?||'';", (name, level))
    before = cur.fetchall()
    return before

def getLevelStarsEarned(name, level):
    cur.execute("SELECT StarsEarned FROM LEVELS WHERE Owner LIKE '%'||?||'%' AND Level = ''||?||'';", (name, level))
    before = cur.fetchall()
    return before

def getPlayerPlanes(name):
    cur.execute("Select Name FROM PLAYERPLANES WHERE Owner LIKE '%'||?||'%';", (name, ))
    before = cur.fetchall()
    return before

def getPlayerPlanesUpgrades(name, plane):
    cur.execute("Select Upgrade FROM PLAYERPLANEUPGRADES WHERE Owner LIKE '%'||?||'%' AND Plane LIKE '%'||?||'%' ;", (name,plane ))
    before = cur.fetchall()
    return before

def getPlayerPlanesUpgradesIcon(name, plane):
    cur.execute("Select Icon FROM PLAYERPLANEUPGRADES WHERE Owner LIKE '%'||?||'%' AND Plane LIKE '%'||?||'%' ;", (name,plane ))
    before = cur.fetchall()
    return before

def getPlayerPlaneUpgrades(name, upgrade, plane ):
    cur.execute("Select Upgrade FROM PLAYERPLANEUPGRADES WHERE Owner LIKE '%'||?||'%' AND Plane LIKE '%'||?||'%' AND Upgrade LIKE '%'||?||'%' ;", (name, plane, upgrade ))
    before = cur.fetchall()
    return before

def printAllPlayerPlanesUpgrades():
    cur.execute("""SELECT * FROM PLAYERPLANEUPGRADES""")
    before = cur.fetchall()
    for i in before:
        print(i)

def printAllPlayer():
    cur.execute("""SELECT * FROM PLAYER""")
    before = cur.fetchall()
    for i in before:
        print(i)



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
            plane CHAR(20),
            Icon INT
        )
        """
                        )
    print("Successfully created player plane upgrade")

def createLevelTable():
    table = cur.execute("""
        CREATE TABLE LEVELS(
            Owner CHAR(20),
            StarsEarned INT,
            MaxScore INT,
            Level INT,
            Completed BOOLEAN
        )
        """
                        )
    print("Successfully created player plane upgrade")


def closeConnection():
    print("closed connection")
    conn.commit()
    conn.close()
