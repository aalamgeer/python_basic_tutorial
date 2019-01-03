class Employee:
	leaves = 10  # class variable 
	
	def __init__(self, name, salary, work): #self is object name, This constuctor call when object create of class
		self.name = name
		self.salary = salary
		self.work = work
		
	def no_leaves(self):
		return self.name + '=' + str(self.leaves)
		
	def printdetails(self):
		print(" The name is {}  Salary is  {} leaves is {} ".format(self.name, self.salary, self.leaves) )
		
	@classmethod
	def change_leaves(cls, newleaves):  # classmethod can access only class variable, it can be access via object or class.
		 cls.leaves = newleaves   		# classmethod don't use self keyword(No object pass in it) it use cls
										# classmethod can be used as alternative constructor
	@classmethod
	def from_str(cls, string):
		#param = string.split("-")  # retrun list from this
		#return cls(param[0], param[1], param[2])
		return cls(*string.split("-"))
		


rana = Employee.from_str("Rana-420-Thugs") # classmethod can be used as alternative constructor
print(rana.name)
print(rana.salary)
print(rana.work)

