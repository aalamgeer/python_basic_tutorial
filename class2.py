class Employee:
	leaves = 10  # class variable 
	
	def __init__(self, aname, alname, asalary): #self is object name, This constuctor call when object create of class
		self.name = aname
		self.lname = alname
		self.salary = asalary
		self.leaves = 20  # If this variable set no_leaves method pick this otherwise class variable using (leaves)
		
	def no_leaves(self):
		return self.name + '=' + str(self.leaves)
	
aalam = Employee("Rohan","Singh",444)
rohan = Employee("AAlam","Rana",555)

print(aalam.no_leaves())

#Employee.leaves = 20

#print(rohan.leaves)
#print(aalam.leaves)