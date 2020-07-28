import tkinter as tk
from uuid import uuid4
import db

class App(tk.Frame):
	def __init__(self, master=None):
		self.__master = master
		self.__master.title('Library')
		self.__master.resizable(False, False)
		self.__init_components()
		self.__load_books(db.select_books())


	def __init_components(self):
		self.__menubar = tk.Menu(self.__master)
		self.__master.config(menu=self.__menubar)

		self.__file_menu = tk.Menu(self.__menubar, tearoff=0)
		self.__file_menu.add_command(label='Exportar BD')
		self.__file_menu.add_command(label='Exportar libro')

		self.__search_menu = tk.Menu(self.__menubar, tearoff=0)
		self.__search_menu.add_command(label='Buscar')

		self.__session_menu = tk.Menu(self.__menubar, tearoff=0)
		self.__session_menu.add_command(label='Username')
		self.__session_menu.add_command(label='Tipo de usuario')
		self.__session_menu.add_separator()
		self.__session_menu.add_command(label='Iniciar sesión')

		self.__mylibrary_menu = tk.Menu(self.__menubar, tearoff=0)
		self.__mylibrary_menu.add_command(label='Ir a mi librería')

		self.__help_menu = tk.Menu(self.__menubar, tearoff=0)
		self.__help_menu.add_command(label='Ir a documentación')

		self.__menubar.add_cascade(label="Archivo", menu=self.__file_menu)
		self.__menubar.add_cascade(label="Buscar", menu=self.__search_menu)
		self.__menubar.add_cascade(label="Sesión", menu=self.__session_menu)
		self.__menubar.add_cascade(label="Mi librería", menu=self.__mylibrary_menu)
		self.__menubar.add_cascade(label="Ayuda", menu=self.__help_menu)

		self.__canvas = tk.Canvas(self.__master, width=350, height=500)
		self.__left_frame = tk.Frame(self.__canvas)
		self.__scrollbar = tk.Scrollbar(self.__master, command=self.__canvas.yview)
		self.__canvas.config(yscrollcommand=self.__scrollbar.set)
		self.__canvas.pack(side=tk.LEFT, fill=tk.X)
		self.__scrollbar.pack(side=tk.LEFT, fill=tk.Y)
		self.__canvas.create_window((1, 1), window=self.__left_frame)
		self.__left_frame.bind("<Configure>", self.onFrameConfigure)

		self.__right_frame = tk.Frame(self.__master, width=400, height=500)
		self.__right_frame.pack(side=tk.LEFT)

	def onFrameConfigure(self, event):
		self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))

	def __load_books(self, books):
		finalbooks = books[:70]
		for book in finalbooks:
			frame = tk.Frame(self.__left_frame, pady=5)
			title = tk.Label(frame, text=book[1], font=('Helvetica', 11, 'bold'))
			author = tk.Label(frame, text=book[2])
			title.pack()
			author.pack()
			frame.pack(fill=tk.X)