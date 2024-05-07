#Queue
#FIFO (First In, First Out)
import datetime

class queue:
	def __init__(self, name, capacity):
	
		self.name = name
		self.created = datetime.datetime.now()
		
		#Número máximo de elementos que una cola puede contener antes de estar llena
		#Puede ser fijo o variable según la implementación de la cola.
		self.capacity = capacity

		#Cantidad actual de elementos que hay en la cola. 
		#Es importante para verificar si la cola está vacía o llena y para realizar operaciones de seguimiento de elementos.
		self.size = 0
		
		#Almacena los elementos individuales de la cola. 
		#Los elementos se organizan siguiendo el principio FIFO (First In, First Out)
		#Se accede a ellos mediante los métodos enqueue y dequeue.
		self.elements = []
		
		#Indica el primer elemento de la cola, es decir, el elemento que se eliminará cuando se llame al método dequeue. 
		#Puede ser un puntero o una referencia al elemento en la implementación.
		self.front = []

		#Representa el último elemento de la cola, que es donde se agrega un nuevo elemento cuando se utiliza el método enqueue. 
		#Al igual que el frente, puede ser un puntero o una referencia.
		self.final = []

		#Indica si la cola está vacía. 
		#Es útil para verificar si la cola necesita más elementos antes de realizar operaciones de eliminación.
		self.empty = True

		#Indica si la cola ha alcanzado su capacidad máxima. 
		#Esto es importante en colas con capacidad limitada para evitar desbordamientos.
		self.full = False
	
	#Verifica si la cola está vacía o no. 
	#Devuelve un valor booleano que indica si la cola no tiene elementos.
	def isEmpty(self):
		#print("isEmpty")
		
		if self.size == 0: 
			self.empty = True
		elif self.size > 0:
			self.empty = False
		
		return self.empty
		
		
	#Verifica si la cola está llena o no. 
	#Devuelve un valor booleano que indica si la cola no tiene elementos.
	def isFull(self):
		#print("isFull")
		
		if self.size == self.capacity:
			self.full = True
		elif self.size < self.capacity:
			self.full = False
		
		return self.full

	#Agrega un elemento al final de la cola.
	#Coloca un elemento en la parte trasera de la fila.
	def enqueue(self, element):
		#print("enqueue")
		
		if self.isFull():
			print("Queue Limit")
		else:
			#Se incrementa su tamaño
			self.elements.append(element)
			self.size += 1
		
		#self.show()
	
	#Elimina y devuelve el elemento en el frente de la cola. 
	#Elimina el elemento que ha estado en la cola durante más tiempo.
	def dequeue(self):
		#print("dequeue")
		
		if self.isEmpty():
			print("Queue Empty")
		else:
			#Se disminuye su tamaño
			pop = self.elements[0]
			self.elements.pop(0)
			self.size -= 1
			
		return pop
		#self.show()
		
	def swap(self,current,new):
		#print("swap")
		
		if self.isEmpty():
			print("Queue Empty")
		elif current >= 0 and current < self.capacity:
			if new >= 0 and new < self.capacity:
				self.elements[current], self.elements[new] = self.elements[new], self.elements[current]
			else:
				print("New: Index out of the range")	
		else:
			print("Current: Index out of the range")	
	
	def show(self):
		n = 0
		if self.isEmpty():
			print("Queue Empty")
		else:
			for x in self.elements:
				print(n, x)
				n += 1
			print("")
			
	def emptyQ(self):
		self.size = 0
		self.elements = []
		self.front = []
		self.final = []
		self.empty = True
		self.full = False
		
	def reset(self,name, capacity):
		self.name = name
		self.created = datetime.datetime.now()
		self.capacity = capacity
		self.size = 0
		self.elements = []
		self.front = []
		self.final = []
		self.empty = True
		self.full = False
#TEST

"""	
cola = queue()

x = {
"book1" : ["task1", "task2", "task3"],
"book2" : ["task1", "task2", "task3"]
}

y = {
"tasker1" : ["task1", "task2", "task3"],
"tasker2" : ["task1", "task2", "task3"]
}



for n in range(31):
	cola.enqueue(x)

cola.enqueue(y)#32
#print(cola.front)
#print(cola.final)
cola.show()

cola.swap(2,31)
cola.show()

cola.enqueue(y)
"""



