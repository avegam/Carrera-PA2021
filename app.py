from tkinter import ttk
from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps
from database_setup import Base, Corredor


# Connect to Database and create database session
engine = create_engine('sqlite:///blog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
#-----------------------
class Carreras:
	
	def __init__(self,window):
		#self.wind = window
		self.notebook = ttk.Notebook(window)
		self.notebook.pack(fill='both',expand='yes')
		self.wind = ttk.Frame(self.notebook)		
		self.notebook.add(self.wind,text = 'ingreso y visualizacion de corredores')
		#self.wind.title('titulo')

		#crear frame contenedero
		frame = LabelFrame(self.wind,text = 'cosa bonita')
		frame.grid(row = 0 ,column = 0 ,columnspan = 2,pady = 10)
		
		#Nombre input
		Label(frame,text ='Nombre:').grid(row = 1 ,column = 0)
		self.Nombre = Entry(frame)
		self.Nombre.grid(row = 1 ,column = 1)
		
		# Apellido Input
		Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
		self.Apellido = Entry(frame)
		self.Apellido.grid(row = 2, column = 1)
		# Marca Input
		Label(frame, text = 'Marca: ').grid(row = 3, column = 0)
		self.Marca = Entry(frame)
		self.Marca.grid(row = 3, column = 1)
		# Sexo Input
		Label(frame, text = 'Sexo: ').grid(row = 4, column = 0)
		self.Sexo = Entry(frame)
		self.Sexo.grid(row = 4, column = 1)
		# T1 Input
		Label(frame, text = 'T1: ').grid(row = 5, column = 0)
		self.T1 = Entry(frame)
		self.T1.grid(row = 5, column = 1)
		# T2 Input
		Label(frame, text = 'T2: ').grid(row = 6, column = 0)
		self.T2 = Entry(frame)
		self.T2.grid(row = 6, column = 1)
		# Mejor Tiempo Input
		#Label(frame, text = 'Mejor Tiempo: ').grid(row = 7, column = 0)
		#self.MejorTiempo = Entry(frame)
		#self.MejorTiempo.grid(row = 7, column = 1)
		# Promedio Input
		#Label(frame, text = 'Promedio: ').grid(row = 8, column = 0)
		#self.Promedio = Entry(frame)
		#self.Promedio.grid(row = 8, column = 1)
		
		# Button Add Product 
		ttk.Button(frame, text = 'Salvar corredor', command = self.add_corredores).grid(row = 9, columnspan = 2, sticky = W + E)
		
		# Output Messages 
		#self.message = Label(text = '', fg = 'red')
		#self.message.grid(row = 12, column = 0, columnspan = 2, sticky = W + E)
		
		# Table
		
		self.tree = ttk.Treeview(frame,height = 8, columns = ('#0','#1','#2','#3','#4','#5','#6','#7','#8'))

		self.tree.grid(row = 12, column = 0, columnspan = 2, sticky = W + E)
		self.tree.heading('#0', text = 'Id', anchor = CENTER )
		self.tree.column("#0", width=50, minwidth=50)
		self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
		self.tree.column("#1", width=150, minwidth=50)
		self.tree.heading('#2', text = 'Apellido', anchor = CENTER)
		self.tree.column("#2", width=150, minwidth=50)
		self.tree.heading('#3', text = 'Marca', anchor = CENTER)
		self.tree.column("#3", width=150, minwidth=50)
		self.tree.heading('#4', text = 'Sexo', anchor = CENTER)
		self.tree.column("#4", width=100, minwidth=50)
		self.tree.heading('#5', text = 'T1', anchor = CENTER)
		self.tree.column("#5", width=50, minwidth=50)
		self.tree.heading('#6', text = 't2', anchor = CENTER)
		self.tree.column("#6", width=50, minwidth=50)
		self.tree.heading('#7', text = 'Mejor Tiempo', anchor = CENTER)
		self.tree.column("#7", width=150, minwidth=50)
		self.tree.heading('#8', text = 'Promedio', anchor = CENTER)
		self.tree.column("#8", width=100, minwidth=50)
		
		
		# Buttons
		#ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
		#ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)
		
		# Filling the Rows
		self.get_corredores()
		
		#Segunda pestaña----------------------------------------------
		self.pestaña2 = ttk.Frame(self.notebook)
		self.notebook.add(self.pestaña2,text = 'Posiciones')
		#self.wind.title('titulo')

		#crear frame contenedero
		frame2 = LabelFrame(self.pestaña2,text = 'cosa')
		frame2.grid(row = 0 ,column = 0 ,columnspan = 2,pady = 10)
		#Label(frame2,text ='Nombre:').grid(row = 1 ,column = 0)
		#self.Nombre = Entry(frame2)
		#self.Nombre.grid(row = 1 ,column = 1)
		
		
		#grilla de posiciones
		self.tree2 = ttk.Treeview(frame2,height = 8, columns = ('#0','#1','#2','#3','#4'))

		self.tree2.grid(row = 12, column = 0, columnspan = 2, sticky = W + E)
		self.tree2.heading('#0', text = 'Id', anchor = CENTER )
		self.tree2.column("#0", width=50, minwidth=50)
		self.tree2.heading('#1', text = 'Nombre', anchor = CENTER)
		self.tree2.column("#1", width=150, minwidth=50)
		self.tree2.heading('#2', text = 'Apellido', anchor = CENTER)
		self.tree2.column("#2", width=150, minwidth=50)
		self.tree2.heading('#3', text = 'Posicion', anchor = CENTER)
		self.tree2.column("#3", width=150, minwidth=50)
		self.tree2.heading('#4', text = 'Mejor Tiempo', anchor = CENTER)
		self.tree2.column("#4", width=150, minwidth=50)
		self.get_posiciones()
		
		
		#Pestaña 3---------------------------------------------
		
		self.pestaña3 = ttk.Frame(self.notebook)
		self.notebook.add(self.pestaña3,text = 'El ultimo en llegar')


		#crear frame contenedero
		frame3 = LabelFrame(self.pestaña3,text = 'cosa cosa')
		frame3.grid(row = 0 ,column = 0 ,columnspan = 2,pady = 10)
		resultado = self.get_ultimo()
		
		Label(frame3,text =resultado).grid(row = 1 ,column = 0)
		
		#Pestaña 4---------------------------------------------
		
		self.pestaña4 = ttk.Frame(self.notebook)
		self.notebook.add(self.pestaña4,text = 'Cuantos corredores participaron')


		#crear frame contenedero
		frame4 = LabelFrame(self.pestaña4,text = 'cosa cosa')
		frame4.grid(row = 0 ,column = 0 ,columnspan = 2,pady = 10)
		resultado = self.get_participantes()
		
		Label(frame4,text =resultado).grid(row = 1 ,column = 0)
		
		#Pestaña 5---------------------------------------------
		
		self.pestaña5 = ttk.Frame(self.notebook)
		self.notebook.add(self.pestaña5,text = 'El peor tiempo de vuelta')


		#crear frame contenedero
		frame5 = LabelFrame(self.pestaña5,text = 'cosa cosa')
		frame5.grid(row = 0 ,column = 0 ,columnspan = 2,pady = 10)
		resultado = self.get_peortiempo()
		
		Label(frame5,text =resultado).grid(row = 1 ,column = 0)
	
	def get_participantes(self):
		corredores = session.query(Corredor).count()
		
		resultado = str(corredores) + " Corredores participan del evento"
		return resultado
		
	def get_peortiempo(self):
		corredores = session.query(Corredor).order_by(Corredor.mejor_tiempo.desc())
		for corredor in corredores:
			resultado = "el peor tiempo de vuelta fue de:" + corredor.nombre + " " + corredor.apellido
			break 
		return resultado

	def get_ultimo(self):
		corredores = session.query(Corredor).order_by(Corredor.promedio.desc())
		for corredor in corredores:
			resultado = "el ultimo en llegar fue: " + corredor.nombre + " " + corredor.apellido
			break 
		return resultado
	
	def get_posiciones(self):
		corredores = session.query(Corredor).order_by(Corredor.mejor_tiempo.desc())
		x = 1
		for corredor in corredores:
			self.tree2.insert('', 0, text = corredor.id, values = (corredor.nombre, corredor.apellido, x, corredor.mejor_tiempo))
			x = x + 1
	
	def get_corredores(self):
		
		# limpia la Tabla 
		self.limpia_record()
		#cargando tabla
		post = session.query(Corredor).all()
		for po in post:
			self.tree.insert('', 0, text = po.id, values = (po.nombre, po.apellido, po.marca, po.sexo, po.t1, po.t2, po.mejor_tiempo, po.promedio))
			
	def add_corredores(self):
		# se decide el mejor tiempo de las 2 vueltas
		if int(self.T1.get()) < int(self.T2.get()):
			mejortiempo = self.T1.get()
		else:
			mejortiempo = self.T2.get()
		#sumo las 2 vueltas y lo divido por 2
		promedio = int(self.T2.get()) + int(self.T1.get())
		promedio = promedio / 2
		NuevoCorredor = Corredor(
				nombre = self.Nombre.get(),
				apellido = self.Apellido.get(),
				marca = self.Marca.get(),
				sexo = self.Sexo.get(),
				t1 = self.T1.get(),
				t2 = self.T2.get(),
				mejor_tiempo = mejortiempo,
				promedio = promedio)
		session.add(NuevoCorredor)
		session.commit()
		self.get_corredores()
		self.get_posiciones()
		
		
	def limpia_record(self):
		#limpia la tabla
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		
			
if __name__ == '__main__':
	window = Tk()
	#window.geometry('500x500')
	aplication = Carreras(window)
	window.mainloop()
