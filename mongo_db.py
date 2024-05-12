
# Step 1:
# -------------------------------------------------------------------------------------------------
import pymongo

import datetime

# Connect to your Atlas cluster
# (use the connection string provided to you during Atlas account setup)
client = pymongo.MongoClient("mongodb+srv://amysaad98:8876873333@gradebook.gisyiki.mongodb.net/?retryWrites=true&w=majority&appName=gradebook")

# Step 2:
# -------------------------------------------------------------------------------------------------

studentsDB = client["<yourDatabaseName>"] # use the name of YOUR database
# If your database name isn’t working, try using the Project Name (the
# default name should be Project0 I think. If that doesn’t work, make a new
# database following the steps provided in the separate PDF.

firstcollection = studentsDB["firstCollection"]
print(client.list_database_names()) # this will show all database names
    

print("Done")

# Step 3:
# -------------------------------------------------------------------------------------------------

firstDocument = {
    "name": {"first": "Ray", "last": "Red"},
    "birthdate": datetime.datetime(2004, 6, 23),
    "courses": ["ENGL102", "MATH151", "COMP121", "CHEM101"],
    "status": "Freshman",
    "gpa": 3.8,
    "grade": "A"
    }

# insert the document into the collection
# firstcollection.insert_one(firstDocument)

# Step 4: 
# -------------------------------------------------------------------------------------------------

# create two new documents to be inserted simultaneously
documents = [
    {
    "name": {"first": "Bella", "last": "Blue"},
    "birthdate": datetime.datetime(2005, 2, 28),
    "courses": ["ENGL102", "MATH151", "COMP325", "BIO201"],
    "status": 'Sophomore',
    "gpa": 3.2,
    "grade": 'B+'
    },
    {
    "name": {"first": "Gary", "last": "Green"},
    "birthdate": datetime.datetime(2003, 1, 15),
    "courses": ["PSYC100", "MATH251", "PHYS121", "COMP325"],
    "status": 'Junior',
    "gpa": 2.8,
    "grade": 'C+'
    }
]

# firstcollection.insert_many(documents)

# Step 5:
# -------------------------------------------------------------------------------------------------

# find the document that matches the search criteria
result = firstcollection.find_one({ "name.last": "Red" })

# print the results
print("Document found:\n", result)

# Step 6:
# -------------------------------------------------------------------------------------------------

'''
Q1: What are the differences between making a connection to a SQLite database and a MongoDB (Atlas)
database? How did we make a new database initially with both (a brief high level explanation only)? What
Python code did we use to connect to and to close both in a .py file? What similarities did you notice, if any?

Differences: In SQLite, connections are made directly to the database using sqlite3 library. In MongDB, connections
are made using the connection string in Atlas and uses the PyMongo library.

Creating a database: In SQLite, a new database is created when connecting to a database file that doesn't exist. In 
MongoDB, a new database is created through the Atlas web interface.

Python code for SQLite:
import sqlite3
conn = sqlite3.connect('example.db')
conn.close()

Python code for MongoDB:
import pymongo
client = pymongo.MongoClient(<yourconnectionstring>)
client.close()

Similarities: Both require database libraries to establish a connection, and both have establishing a connection 
and closing it when done

Q2: What is the differences between inserting single and multiple rows/documents of data into a SQLite vs
MongoDB table/collection? Does one seem easier over the other?

In SQLite, single/multiple rows of data are inserted using "INSERT INTO," and in MongoDB, single documents are
inserted using "inser_many()" method. For ease, I think MongoDB is better for flexibility and SQLite is
better for simplicity.

Q3: What do you think of the difference in the data structures between a relational table and a collection of
documents: What advantages and/or disadvantages can you imagine with each data structure? And which
do you prefer so far (and why)?

Difference: Relational table vs collection of documents

Advantages and Disagvantages: Relational table vs Collection of documents

Relational table:
A: good structure and good for complex queries
D: may need migrations for changes

Collection of documents:
A: flexible and good for unstructured data
D: data duplication

I prefer relation tables for the way it handles data.

Q4: Make a prediction: which database do you think will be easier to automate the data insertion process for
(like from a csv file to the database)?

I think MongoDB might be easier to automate the date insertion process because of its flexibility.
It allows for an easy displaying of the various source documents. I also think the "mongoimport"
tool helps so that it gives a straightforward method for importing data from a CSV file.

'''