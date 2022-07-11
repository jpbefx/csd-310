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
    player = [] 
    team = []
    cursor = db.cursor()

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


#    cursor.execute("SELECT team_id, team_name, mascot FROM team INNER JOIN player ON player.team_id = team.team_id;")
#    print('-- DISPLAYING TEAM RECORDS --')
#    for teams in cursor:
#       print(teams)
#       
#       #print("Team ID: {}\nTeam Name: {}\nMascot: {}".format(team['team_id'], team['team_name'], team['mascot']))
#        
#    print()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    print('-- DISPLAYING INNER JOIN RESULTS --')
    for players in cursor:
        print(players)
#       
        #print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}".format(players['player_id'], players['first_name'], players['last_name'], players['team_name']))


    db.close()