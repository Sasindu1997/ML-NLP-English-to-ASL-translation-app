from tinydb import TinyDB, Query
db = TinyDB('db.json')

db.insert({'name': 'i', 'path': 'i.mp4'})
db.insert({'name': 'go', 'path': 'go.mp4'})
db.insert({'name': 'home', 'path': 'home.mp4'})
db.insert({'name': 'yes', 'path': 'yes.mp4'})
db.insert({'name': 'no', 'path': 'no.mp4'})
db.insert({'name': 'hello', 'path': 'hello.mp4'})


db.insert({'name': 'how', 'path': 'how.mp4'})
db.insert({'name': 'fine', 'path': 'fine.mp4'})
db.insert({'name': 'good', 'path': 'good.mp4'})
db.insert({'name': 'you', 'path': 'you.mp4'})

