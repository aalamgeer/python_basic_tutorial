class Employee:
	leaves = 10
	
	def __init__(self, name, salary, work):
		self.name = name
		self.salary = salary
		self.work = work
	
	def whoisthis():
		return "Employee class"

class student(Employee):
	
	def __init__(self):
		#print "This is student class"
		super().__init__("Aalm",1452,"Engineer")
		
		
st = student()
