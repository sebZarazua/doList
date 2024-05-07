import datetime

class task():

	def __init__(self,name):
		self.name = name
		self.note = ""
		self.lim = datetime.datetime.now()
		self.priority =  "default"
		self.list = []
		self.list.append(self.name)
		self.list.append(self.note)
		self.list.append(self.lim.strftime("%Y")+self.lim.strftime("%m")+self.lim.strftime("%d")+self.lim.strftime("%H")+self.lim.strftime("%M"))
		self.list.append(self.priority)
	
	def update(self):
		self.list = []
		self.list.append(self.name)
		self.list.append(self.note)
		self.list.append(self.lim.strftime("%Y")+self.lim.strftime("%m")+self.lim.strftime("%d")+self.lim.strftime("%H")+self.lim.strftime("%M"))
		self.list.append(self.priority)
	
	def setName(self, name):
		self.name = name;
		self.list[0] = self.name
		
	def setNote(self, note):
		self.note = note;
		self.list[1] = self.note
			
	def setLim(self, year, month, day, hour, minute): #YYYY MM MM
		self.lim = datetime.datetime(year, month, day, hour, minute)
		self.list[2] = self.lim.strftime("%Y")+self.lim.strftime("%m")+self.lim.strftime("%d")+self.lim.strftime("%H")+self.lim.strftime("%M")
	
	def setPriority(self, priority):
		self.priority = priority;
		self.list[3] = self.priority
