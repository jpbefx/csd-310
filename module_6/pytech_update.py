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

# Print a header for information as to what is being displayed
print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")

# Find all of the document contents
for module6_2 in collection.find({},{'_id':0}):
    print(module6_2)

# call the update_one method by student_id 1007 and 
# update the last name to something different than the originaly saved name.
m6_2Update = collection.update_one({"Student_ID": "1007"}, {"$set": {"Last Name": "Bond"}})

print()
print()

# Print a header for information as to what is being displayed
print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")

# Display updated student document from find_one query
alterEgo = collection.find_one({"Student_ID": "1007"}, {"_id":0})

print(alterEgo)

