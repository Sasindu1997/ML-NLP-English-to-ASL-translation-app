from tinydb import TinyDB, Query
db = TinyDB('db.json')

db.insert({'name': 'i', 'path': ''})
db.insert({'name': 'go', 'path': ''})
db.insert({'name': 'home', 'path': ''})
db.insert({'name': 'yes', 'path': ''})
db.insert({'name': 'no', 'path': ''})
db.insert({'name': 'hello', 'path': ''})

# db.all()
#
# for item in db:
#      print(item)

# Fruit = Query()
# res = db.search(Fruit.type == 'peach')
# print(res)

# db.truncate()