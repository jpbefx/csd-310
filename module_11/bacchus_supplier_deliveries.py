#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#07/17/2022
#Module 11.1 Assignment: Milestone #3

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "bacchus_user",
	"password": "bacchus",
	"host": "127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

stmt = "SELECT deliveries_log.shipment_id, deliveries_log.expected_delivery_date, deliveries_log.actual_delivery_date, supplies.supply_name, suppliers.supplier_name FROM deliveries_log INNER JOIN suppliers ON deliveries_log.supplier_id = suppliers.supplier_id INNER JOIN supplies ON suppliers.supplier_id = supplies.supplier_id"

cursor.execute(stmt)
ret = cursor.fetchall()
print("\nSupply Orders Incoming Joined Across All Tables")
print("*************************************************************************************************************\n")

print("Ship ID: | Exp Del Date:| Act Del Date: | Supply: \t| Supplier:")
for re in ret:
    print(str(re[0]) + "\t | " + str(re[1]) + " \t| " + str(re[2]) + " \t| " + str(re[3]) + "      \t| " + str(re[4]))

print("\n*************************************************************************************************************")