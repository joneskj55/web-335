# ========================================
# Title: Exercise 9.3
# Author: Kevin Jones
# Date: 10 May 2021
# Description: Updating and Deleting Documents
# ========================================

# import MongoClient, pprint & datetime
from pymongo import MongoClient
import pprint
import datetime

# connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# update email address of document created in 9.2 to my Bellevue address
db.users.update_one(
    {"employee_id": "837736"},
    {
        "$set": {
            "email": "kevjones@my365.bellevue.edu"
        }
    }
)

# print the document using the find_one query
pprint.pprint(db.users.find_one({"email": "kevjones@my365.bellevue.edu"}))
