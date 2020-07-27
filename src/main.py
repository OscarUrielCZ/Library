from tkinter import Tk
from uuid import uuid4
from App import App
from User import User
import db

if __name__ == '__main__':
	# db.insert_user(User('Oscar', '1234', str(uuid4())))
	db.delete_user('ec7e34d4-af44-4624-9414-4df413207a1e')
	# root = Tk()
	# App(master=root)
	# root.mainloop()