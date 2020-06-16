import sqlite3

db = sqlite3.connect('contacts.db')

cur = db.cursor()

def __iter(self,db):
    self.db = db
    return db


db.commit()
db.close()