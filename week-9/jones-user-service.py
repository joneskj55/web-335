# ========================================
# Title: Exercise 9.2
# Author: Kevin Jones
# Date: 10 May 2021
# Description: Querying and Creating Documents
# ========================================

# import MongoClient, pprint & datetime
from pymongo import MongoClient
import pprint
import datetime

# connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# create a new user document
user = {
    "first_name": "Kevin",
    "last_name": "Jones",
    "email": "me@mail.com",
    "employee_id": "837736",
    "date_created": datetime.datetime.utcnow()
}

# insert the user document
user_id = db.users.insert_one(user).inserted_id

# output the user_id
print(user_id)

# print the document using the find_one query
pprint.pprint(db.users.find_one({"employee_id": "837736"}))
