'''
I thought that working with mongo db was actually a lot easier,
maybe just because vscode decided to work well today but I dont know.
It was harder to connect to mongodb and I had to fiddle with it to make it work and I have more to do
but overall I enjoyed mongodb a lot more
'''

import os
import sqlite3
import pymongo
from dotenv import load_dotenv

DB_FILEPATH = (os.path.join(os.path.dirname(__file__), '..', 'u3S1day1', 'rpg_db.sqlite3'))

connection = sqlite3.connect(DB_FILEPATH)

connection.row_factory = sqlite3.Row
cursor = connection.cursor()

#make dictionaries for each row in charactercreator_character
query = 'SELECT * FROM charactercreator_character'
cursor.execute(query)
result = cursor.fetchall()

character_rows = [dict(row) for row in result]

# make dict for each row in armory item
query = 'SELECT * FROM armory_item'
cursor.execute(query)
result = cursor.fetchall()
item_rows = [dict(row) for row in result]




load_dotenv()

connection_uri = f"donthackme"

client = pymongo.MongoClient(connection_uri)

db = client.Module3_db 

# insert characters into db
collection1 = db.characters 
collection1.insert_many(character_rows)

# insert items into db
collection2 = db.items
collection2.insert_many(item_rows)
