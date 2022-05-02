from tinydb import TinyDB, Query
db = TinyDB('db.json')

db.all()

queue = []

for item in db:
    print(item)


def viewAllSigns():
    for data in db:
        queue.append(data)

    return queue
