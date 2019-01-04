class Employee:
	leaves = 10  # class variable 
	
	def __init__(self, aname, alname, asalary): #self is object name, This constuctor call when object create of class
		self.name = aname
		self.lname = alname
		self.salary = asalary
		self.leaves = 20  # If this variable set, no_leaves method pick this, otherwise use leaves class variable.
		
	def no_leaves(self):
		return self.name + '=' + str(self.leaves)
		
	def printdetails(self):
		print(" The name is {}  Salary is  {} leaves is {} ".format(self.name, self.salary, self.leaves) )
	
aalam = Employee("AAlam","Singh",444)
rohan = Employee("Rohan","Rana",555)

#print(aalam.no_leaves())
#print(rohan.no_leaves())

#print(rohan.__dict__) # To check instance variable of rohan instance
#print(aalam.__dict__) # To check instance variable of Aalam instance

#Employee.leaves = 20

print(rohan.printdetails)