import sqlite3

connection = sqlite3.connect('sample.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER
               )
''')

connection.commit()