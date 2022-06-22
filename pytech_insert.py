#### James Bailey CSD 310 Module 5 pytech_insert.py  ####


# importing Mongoclient from pymongo
from pymongo import MongoClient
 
# Make a variable to hold the Connection Key URL 
url = "mongodb+srv://admin:admin@cluster0.pvrfn.mongodb.net/?retryWrites=true&w=majority";

# Make connection
client = MongoClient(url)

# Database Variable
db = client.pytech

# Switch to collection
collection = db["students"]
 
# Creating Dictionary of records to be inserted
James = {"Student_ID": "1007",
          "First Name": "James",
          "Last Name" : "Bailey"}
          
Caleb = {"Student ID": "1008",
         "First Name": "Caleb",
         "Last Name": "Rummel"}

Christeen = {"Student ID": "1009",
             "First Name": "Christeen",
             "Last Name": "Safar"}

james_id = collection.insert_one(James).inserted_id

print(james_id)

caleb_id = collection.insert_one(Caleb).inserted_id

print(caleb_id)

christeen_id = collection.insert_one(Christeen).inserted_id

print(christeen_id)

