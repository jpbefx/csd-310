import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "CSD310",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    player = {} 
    team = {}
    cursor = db.cursor(dictionary=True)

    print("\n   Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press <ENTER> key to continue...")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" the supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" the specified database does not exist")

    else:
        print(err)

finally:
    print("Program Connected with no errors.")

    print("INSERTING TABLE...")

    cursor.execute("INSERT INTO player(first_name, last_name, team_id)\
        VALUES('Smeagol', 'Shire Folk', 1)")


    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    print("\n--  DISPLAYING PLAYERS AFTER INSERT --\n")
    for players in cursor:
        players

        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n\n".format(players['player_id'], players['first_name'], players['last_name'], players['team_name']))


    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    print("\n--  DISPLAYING PLAYERS AFTER UPDATE --\n")
    for players in cursor:
        players

        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n\n".format(players['player_id'], players['first_name'], players['last_name'], players['team_name']))


    cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol';")
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    print("\n--  DISPLAYING PLAYERS AFTER DELETE --\n")
    for players in cursor:
        players

        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n\n".format(players['player_id'], players['first_name'], players['last_name'], players['team_name']))

    
    db.close()