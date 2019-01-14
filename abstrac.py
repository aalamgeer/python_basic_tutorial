class Employee:
	leaves = 10
	
	def __init__(self, name, salary, work):
		self.name = name
		self.salary = salary
		self.work = work
		
#Abstraction is concept of collection of many task into one task, And comman task perform methods declare in abstrct class
		
aalam = Employee("Aalam", 1000, "Engineer")

print(aalam)
