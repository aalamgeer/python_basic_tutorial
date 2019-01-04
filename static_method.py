class Employee:
	leaves = 10
	
	def __init__(self, name, salary, work):
		self.name = name
		self.salary = salary
		self.work = work
		
	@staticmethod
	def printgood(): # No need to pass self in static method
		print("This printgood static method, It does't take cls(class) and self(object) as argument " )
		return "Return values here"
		
aalam = Employee("Aalam", 1000, "Engineer")

print(aalam)
aalam.printgood()
print(Employee.printgood())