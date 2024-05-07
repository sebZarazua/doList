import toDo as td
import queue as qu
import task as ts
import datetime
import os
import time

class menu:
	#def __init__(self):
	#main
	#	->tasks
	#		->options
	def main(self):
		menu = True

		while menu == True:
			os.system("clear")
			print("\tTo Do List\n")
			print("+ New")
			print("* Open")
			print(". Exit\n")

			op = input()
			if op == "+":
				
				print("\nName:")
				name = input()
				print("\nSelect Capacity:")
				print("8")
				print("16")
				print("32")
				capacity = input()
				tdList = td.toDo(name, int(capacity))
				print("New List Created")
				self.tasks(tdList)
			elif op == "*":
				for file in os.listdir():
					if file.endswith('.txt'):
						print(file)
				name = input()	
				tdList = td.toDo(name, 0)
				tdList.read(name)
				self.tasks(tdList)
			elif op == ".":
				tdList.save()
				menu = False
	
		
	def tasks(self, tdList):
		listMenu = True

		while listMenu == True:
			os.system("clear")
			print("\t",tdList.name, "\n")
			taskList = tdList.get()
			for n in range(len(taskList)):
				print(n, "] ",taskList[n][0])
				print("\t|->", taskList[n][3])
				if taskList[n][1] != "":
					print("\t|->", taskList[n][1])
				#print("\t|->",taskList[n][2][8:10],":",taskList[n][2][10:12], " " ,taskList[n][2][6:8], "/", taskList[n][2][4:6], "/", taskList[n][2][0:4])
				#print("\t|->", taskList[n][3])
				print("")
			print("\n")
			print("+ Task")
			print("- Task")
			print("% Swap")
			print("^ Back")
			print(". Save\n")
			
			op = input()
				
			match op:
				case "+":
					print("Task name:")
					name = input()
					newTask = tdList.task(name)
					tdList.save()
				case "-":
					print("What task do you want to delete?")
					pos = input()
					if pos.isdigit():
						n = int(pos)
						print("Are you sure you want to delete? y/n")
						delOp = input()
						if delOp == "y":
							tdList.doList.elements[int(n)].priority = "high"
							tdList.doList.swap(int(n),int(0))
							print(tdList.doList.dequeue())
				case "%":
					print("Current Position: ")
					currnt = input()
					print("New Position: ")
					new = input()
					tdList.doList.swap(int(currnt),int(new))
					tdList.save()
				case "^":
					listMenu = False
				case ".":
					tdList.save()
				case _:
					if op.isdigit():
						
						self.options(op, tdList)
					else:
						print("Incorrect Option... Try Again (c:) ")
						time.sleep(3)
	def options(self, n, tdList):
		opMenu = True
		
		while opMenu == True:
			os.system("clear")
			print("\t",tdList.name)
			print("\t|->",tdList.doList.elements[int(n)].name, "\n")
			print("Note: ", tdList.doList.elements[int(n)].note)
			print("Priority: ", tdList.doList.elements[int(n)].priority)
			print("Limit Date: ", tdList.doList.elements[int(n)].lim)
			print("")
			print("~ Rename")
			print(": Note")
			print("< Priority")
			print("° Limit Date")
			print("^ Back")
			
			op = input()
			
			match op:
				case "~":
					print("New name:")
					name = input()
					tdList.doList.elements[int(n)].name = name
				case ":":
					print("Insert Note:")
					note = input()
					tdList.doList.elements[int(n)].note = note
				case "<":
					print("Select Priority:")
					print("0) default")
					print("1) high")
					print("2) medium")
					print("3) low")
					priority = input()
					match int(priority):
						case 0:
							tdList.doList.elements[int(n)].priority = "default"
						case 1:
							tdList.doList.elements[int(n)].priority = "high"
						case 2:
							tdList.doList.elements[int(n)].priority = "medium"
						case 3:
							tdList.doList.elements[int(n)].priority = "low"
						case _:
							tdList.doList.elements[int(n)].priority = "default"
					
				case "°":
					print("Year:")
					print("example 2001")
					year = input()
					print("Month:")
					print("example 01")
					month = input()
					print("Day:")
					print("example 01")
					day = input()
					print("Hour:")
					print("example 12")
					hour = input()
					print("Minute:")
					print("example 30")
					minute = input()
					tdList.doList.elements[int(n)].lim = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
				case "^":
					opMenu = False
				case _:
					print("Incorrect Option... Try Again (c:) ")
					time.sleep(3)
dl = menu()
dl.main()

