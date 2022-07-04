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
    print("Program Finished with no errors.")
    
    db.close()