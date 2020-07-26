from os import path
import sqlite3
from User import User

database_name = 'library.db'
database =path.join('../db/', database_name)

def create_user(user):
	connection = sqlite3.connect('../')
	cursor = connection.cursor()

	#try:
		#cursor.execute(f'INSERT INTO users VALUES ()')
	# connection.commit()
	connection.close()