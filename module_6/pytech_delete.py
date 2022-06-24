#### James Bailey CSD 310 Module 6.3 pytech_delete.py  ####


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
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Find all of the document contents
for module6_3 in collection.find({},{'_id':0}):
    print(module6_3)
print()
print()


# Print a header for information as to what is being displayed
print("-- INSERT STATEMENTS --")
# Call the insert_one() method and Insert a new document 
# into the pytech collection with student_id 1010.
collection.insert_one({"Student_ID": "1010",
          "First Name": "Ed",
          "Last Name" : "Harley"})


newDoc = collection.find_one({"Student_ID": "1010"})
print("Inserted student record 1010 into the students collection")
print(newDoc)
# Print a header for information as to what is being displayed
print("\n\n-- DISPLAYING NEW STUDENT LIST DOC --")
# Find all of the document contents
for module6_3 in collection.find({},{'_id':0}):
    print(module6_3)


# Print a header for information as to what is being displayed
print("\n\n-- DELETED STUDENT ID: 1010 --")

collection.delete_one({"Student_ID": "1010"})

for module6_3 in collection.find({},{'_id':0}):
    print(module6_3)