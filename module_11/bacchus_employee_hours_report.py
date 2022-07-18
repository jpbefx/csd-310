#Caleb Rummel, James Bailey, Joel Mardock, Nicholas Werner
#7-13-2022
#Module 10.2 Assignment
#Initial build by CRummel


import mysql.connector
from mysql.connector import errorcode

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

#Dummy Data for Current Quarter
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-11', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-11', 12);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-08', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-08', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-07', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-07', 10);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-07-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-07-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-07-06', 7);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-07-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-07-06', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-07-06', 8);")

#Dummy Data for Second Quarter
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-06-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-06-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-06-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-06-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-06-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-06-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-06-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-06-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-06-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-06-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-06-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-06-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-06-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-06-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-06-11', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-06-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-06-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-06-11', 12);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-05-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-05-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-05-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-05-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-05-08', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-05-08', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-04-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-04-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-04-07', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-04-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-04-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-04-07', 10);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-04-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-04-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-04-06', 7);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-04-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-04-06', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-04-06', 8);")

#Dummy Data for First Quarter
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-03-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-03-13', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-03-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-03-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-03-13', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-03-13', 12);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-02-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-02-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-02-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-02-12', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-02-12', 3);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-02-12', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-02-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-02-11', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-02-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-02-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-02-11', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-02-11', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-01-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-01-08', 9);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-01-08', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-01-08', 7);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-01-08', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-01-08', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-01-07', 3);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-01-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-01-07', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-01-07', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-01-07', 6);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-01-07', 10);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(1, '2022-01-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(2, '2022-01-06', 8);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(3, '2022-01-06', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(4, '2022-01-06', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(5, '2022-01-06', 4);")
cursor.execute("INSERT INTO employee_time (personnel_id, work_date, hours) VALUES(6, '2022-01-06', 5);")

db.commit()

#Third Quarter Report
cursor.execute("SELECT personnel_id, SUM(hours) quarterly_hours FROM employee_time  WHERE work_date BETWEEN '2022-07-01' AND '2022-07-31' GROUP BY personnel_id;")

print("-- Displaying Current Quarter Hours --")
employee_id = cursor.fetchall()
for employee in employee_id:
    print("Personnel ID: {}".format(employee[0]),
        "\nHours this Quarter: {}\n".format(employee[1]))

#Second Quarter Report
cursor.execute("SELECT personnel_id, SUM(hours) quarterly_hours FROM employee_time  WHERE work_date BETWEEN '2022-04-01' AND '2022-06-30' GROUP BY personnel_id;")

print("-- Displaying Second Quarter Hours --")
employee_id = cursor.fetchall()
for employee in employee_id:
    print("Personnel ID: {}".format(employee[0]),
        "\nHours this Quarter: {}\n".format(employee[1]))

#First Quarter Report
cursor.execute("SELECT personnel_id, SUM(hours) quarterly_hours FROM employee_time  WHERE work_date BETWEEN '2022-01-01' AND '2022-03-31' GROUP BY personnel_id;")

print("-- Displaying Second Quarter Hours --")
employee_id = cursor.fetchall()
for employee in employee_id:
    print("Personnel ID: {}".format(employee[0]),
        "\nHours this Quarter: {}\n".format(employee[1]))

