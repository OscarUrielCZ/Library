from tkinter import Tk
import uuid
from App import App
from User import User
import db

if __name__ == '__main__':
	db.create_user(User('Oscar', '1234', id=str(uuid.uuid4())))
	# root = Tk()
	# App(master=root)
	# root.mainloop()