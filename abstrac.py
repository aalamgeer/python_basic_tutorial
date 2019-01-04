class Employee:
	leaves = 10
	
	def __init__(self, name, salary, work):
		self.name = name
		self.salary = salary
		self.work = work
		
#Abstraction is concept of collection of many task into one task, And to hide the information from user
		
aalam = Employee("Aalam", 1000, "Engineer")

print(aalam)
