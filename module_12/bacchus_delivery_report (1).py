#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#7-13-2022
#Module 10.2 Assignment
#Initial build by CRummel


import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate


config = {
    "user": "root",
    "password": "January-123",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {}" .format(config["user"], config["host"]))
    print("")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

cursor.execute("SELECT *, DATEDIFF(expected_delivery_date, actual_delivery_date) date_difference FROM deliveries_log WHERE expected_delivery_date BETWEEN '2022-01-01' AND '2022-12-31' ORDER BY date_difference;")

#Print in table format
myresult = cursor.fetchall()

print(tabulate(myresult, headers=['Shipment ID', 'Expected Delivery', 'Actual Delivery', 'Supplier ID', 'Date Difference'], tablefmt='psql'))