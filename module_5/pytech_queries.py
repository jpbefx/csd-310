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

# Create a loop to retrieve all of the collection's documents and print each one
for x in collection.find({},{'_id':0}):
    print(x)
print()
print()
# Find only James Bailey in the list of documents inside of the the collection "students"
id_1007 = collection.find_one({"Student_ID": "1007",
                             "First Name": "James",
                             "Last Name" : "Bailey"},{'_id':0})

print(id_1007)