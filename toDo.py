import queue as qu
import task as ts
import datetime
import os


class toDo:
	def __init__(self, name, capacity):
		#queue 
		self.name = name
		self.capacity = capacity
		self.doList = qu.queue(self.name, self.capacity)
		
		if os.path.exists(self.name+".txt"):
			if os.stat(self.name+".txt").st_size==0:
				self.fl = open(self.name+".txt", "r")
				self.fl.close()
			else:
				self.read(self.name)
		else:
			self.fl = open(self.name+".txt", "x")
			self.fl.close()
	def task(self, tName):
		self.newTask = ts.task(tName)
		self.doList.enqueue(self.newTask) 
	
	def get(self):
		#Obtiene una lista de las tareas en cola de una estructura definida
		toDoList = []
		self.order()
		#self.orderDate()
		for tsk in self.doList.elements:
			tsk.update()
			toDoList.append(tsk.list)
		return toDoList
			
	def save(self):
		#Guarda una estuctura de cola y tarea perviamente definidas
		#Retorna lo que se guardó
		output =  str(self.capacity) + str(self.get())
		self.fl = open(self.name+".txt", "w")
		self.fl.write(output)
		self.fl.close()
		return output
	def read(self, name):
		#Lee el archivo y obtiene su contenido
		infile = open(name+".txt","br")	#Lee el archivo en forma binaria para aceptar cualquier extension
		bytes_str = bytes(infile.read())	#Tranforma de binario a tipo bytes para posteriormente
		content = bytes_str.decode("ISO-8859-1")#Decodifica los bytes con ISO-8859-1
		infile.close()				
		
		#Del contenido obtiene un numero que es su capacidad
		outLoop = False
		cap = ""
		for x in content:
			if x == "[":
				outLoop = True
			elif x.isnumeric():
				cap = cap + x
				
			if outLoop == True:
				break
				
		
		#Toma el contenido y lo enlista para poder estructurar de nuevo		
		inKey = False
		keys = 0
		inStr = False
		varStr = ""
		total = []
		for x in content:
			match x:
				case "[":
					keys += 1
					
					if keys > 1:
						newList = []
						inKey = True
				case "'":
					if inStr == False:
						inStr = True
					elif inStr == True:
						newList.append(varStr)
						inStr = False
				case ",":
					continue
				case " ":
					if inStr == True:
						varStr = varStr + x
					elif inStr == False:
						varStr = ""
				case "]":
					if inKey == True:
						total.append(newList)
						inKey = False
				case _:
					if inKey == True:
						varStr = varStr + x
		
		
		#Con el nombre, capacidad y contenido se crea un nuevo objeto o se reestructura
		
		self.name = name
		self.capacity = int(cap)
		self.doList.emptyQ()
		self.doList = qu.queue(self.name, self.capacity)
		
		if keys > 1:
			for n in total:
				
				self.newTask = ts.task(n[0])
				self.newTask.setNote(n[1])
				self.newTask.setLim( int( n[2][0:4] ), int( n[2][4:6] ), int( n[2][6:8] ), int( n[2][8:10] ), int( n[2][10:12] ) )
				self.newTask.setPriority(n[3])
				
				self.doList.enqueue(self.newTask)
		
	def order(self):
		priorities = []
		for task in self.doList.elements:
			if task.priority == "default":
				priorities.append(4)
			elif task.priority == "high":
				priorities.append(1)
			elif task.priority == "medium":
				priorities.append(2)
			elif task.priority == "low":
				priorities.append(3)
		
		#print(priorities)
		order = priorities
		
		for i in range(len(order)):
			for j in range(len(order)):
				#print(i,j)
				if j > i:
					if order[i] > order [j]:
						order[i], order [j] = order[j], order [i]
						self.doList.swap(i,j)
						#print(order)
					#else: print("\t",order)
			#print("\n\n")
		#print(order)
	
	def orderDate(self):
		dates = []
		for task in self.doList.elements:
			dates.append(task.lim)
		
		#print(priorities)
		order = dates
		
		for i in range(len(order)):
			for j in range(len(order)):
				#print(i,j)
				if j > i:
					if order[i] > order [j]:
						order[i], order [j] = order[j], order [i]
						self.doList.swap(i,j)
						#print(order)
					#else: print("\t",order)
			#print("\n\n")
		#print(order)
