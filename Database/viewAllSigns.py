from tinydb import TinyDB, Query
from NLTK.testModel1 import *
from Database.matchingSign import *

db = TinyDB('db.json')

db.all()

queue = []

for item in db:
    print(item)


# def viewallsigns():
#     for item in db:
#         queue.append(item)
#
#     return queue
