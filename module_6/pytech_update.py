#### James Bailey CSD 310 Module 6 pytech_update.py  ####


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

# Find all of the document contents
module6_2 = collection.find()

print(module6_2)