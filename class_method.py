class Employee:
	leaves = 10  # class variable 
	
	def __init__(self, aname, alname, asalary): #self is object name, This constuctor call when object create of class
		self.name = aname
		self.lname = alname
		self.salary = asalary
		self.leaves = 5  # If this variable set no_leaves method pick this otherwise class variable using (leaves)
		
	def no_leaves(self):
		return self.name + '=' + str(self.leaves)
		
	def printdetails(self):
		print("The name is {}  Salary is  {} leaves is {} ".format(self.name, self.salary, self.leaves))
		
	@classmethod
	def change_leaves(cls, newleaves):  # classmethod can access only class variable, it can be access via object or class.
		 cls.leaves = newleaves   		# classmethod don't use self keyword(No object pass in it) it use cls
										# classmethod can be used as alternative constructor
aalam = Employee("AAlam","Singh",444)
rohan = Employee("Rohan","Rana",555)

aalam.change_leaves(21)

print(aalam.leaves)
print(rohan.leaves)
print(Employee.leaves)
print(aalam.__class__.leaves)  # Another way to call class variable via __class__