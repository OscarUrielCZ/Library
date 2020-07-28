from os import listdir
from os.path import isdir, isfile, join
import mysql.connector
import uuid

dirpath = '/media/oscar/KINGSTON/450LibrosSoloParaGenteInteligente.FL'
authors = listdir(dirpath)
config = {
	'user': 'oscar',
	'password': 'Oscarpass1234.',
	'host': '127.0.0.1',
	'database': 'library'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
query = 'INSERT INTO books (id, title, author, description, imguri) VALUES (%s, %s, %s, %s, %s)'
values = []

for author in authors:
    authorpath = join(dirpath, author)
    if isdir(authorpath):
        books = listdir(authorpath)
        for book in books:
            if book.split('.')[-1] == 'zip':
                try:
                    score_index = book.index('-')
                    dot_index = book.rindex('.')
                    title = book[score_index+1:dot_index].strip()
                    values.append((str(uuid.uuid4()), title, author, None, None))
                except ValueError:
                    print('Error in:', book)

cursor.executemany(query, values)
db.commit()
db.close()