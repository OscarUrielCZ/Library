from os import path
import sqlite3
from User import User

database_name = 'library.db'
database = path.join('../db/', database_name)

def create_user(user):
	connection = sqlite3.connect(database)
	cursor = connection.cursor()

	#try:
	cursor.execute(f"INSERT INTO users VALUES ('{user.id}', '{user.username}', '{user.password}')")
	#except:
	#	print('Something went wrong')
	
	print(f'New user singed up: {user.username}')
	connection.commit()
	connection.close()