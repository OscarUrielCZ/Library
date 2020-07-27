from os import path
import mysql.connector
from User import User

config = {
	'user': 'oscar',
	'password': 'Oscarpass1234.',
	'host': '127.0.0.1',
	'database': 'library'
}

def insert_user(user):
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	query = 'INSERT INTO users (id, username, password) VALUES (%s, %s, %s)'
	values = (user.id, user.username, user.password)
	cursor.execute(query, values)
	
	db.commit()
	db.close()

def delete_user(id):
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	query = f"DELETE FROM users WHERE id='{id}'"
	cursor.execute(query)
	
	db.commit()
	db.close()