#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#07-10-2022
#Module 10.3 Assignment

'''This script will select all of the data from each table in the "bacchus" database and output it in print lines'''
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
print("************************************************************************")
print("\n--- Average Units Ordered: All Wine ---") 
# queries for retrieving the average of order_units from wine_distribution table
retrieve = "Select AVG(order_units) AS average FROM wine_distribution;"

# executing the average query
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("\nAverage units ordered is : " + str(i[0]))
print("\n************************************************************************")

print("\n---  Total Units Ordered: All Wine   ---")
# qeuries for retriving the sum of order_units from wine_disribution table
retrieve = "SELECT SUM(order_units) \
            AS total \
    FROM wine_distribution;"

# executing the sum query
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("\nTotal Units ordered is: " + str(i[0]))
print("\n************************************************************************")

print("\n---  Distributor By Wine  ---")
# qeuries for retriving each wine by each distributor
retrieve = "SELECT	order_id, \
		wine_name, \
         distributor_name, \
         order_units \
    FROM	bacchus.wine_distribution;;"

# Header panel for the 'join' table
print("\nID| \tWine |Distributor| Order Qty")

# executing the query separated by | 
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print(i[0], "|", i[1], "|", i[2], "|", i[3])
print("\n************************************************************************")

print("\n---  All Columns From wine_distribution & wine_production  ---")
# queries for retrieving each wine in both wine_production and wine_distribution
cursor.execute('SELECT	* FROM bacchus.wine_distribution, bacchus.wine_production WHERE wine_distribution.wine_name = wine_production.wine_name AND wine_production.units_produced')
cursorVariable = cursor.fetchall()

# Header panel for the 'join' table
print("\nID | Order Dt |  Wine | Qty | Distributor | ID | Wine  | Born on Date | NumProduced\n")

#print("Deliveries_Log" + str(cursor.column_names))
for rows in cursorVariable:
    print( rows[0], "|", rows[1], "|", rows[2], "|", rows[3], "|", rows[4], "|", rows[5], "|", rows[6], "|", rows[7], "|", rows[8])
print("\n************************************************************************")
print("\n---  Joined Columns From wine_distribution & wine_production by wine_name  ---")
# query to join wine_distribution to wine_production using order_id, wine_name, units_produced, distributor_name, order_units
retrieve = "SELECT wine_distribution.order_id, wine_distribution.wine_name, wine_production.units_produced, wine_distribution.distributor_name, wine_distribution.order_units \
            FROM wine_distribution INNER JOIN wine_production ON wine_distribution.wine_name = wine_production.wine_name"
# Header panel for the 'join' table
print("\n(ID, Wine, Qty Produced, Distributor, Qty Ordered)\n")
# execution the join query
cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print(i)

