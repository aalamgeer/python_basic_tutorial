class Employee:
	leaves = 10
	
	def __init__(self, aname, alname, asalary): #self is object name, This constuctor call when object create of class
		self.name = aname
		self.lname = alname
		self.salary = asalary
	
aalam = Employee("Rohan","Singh",444)
rohan = Employee("AAlam","Rana",555)

Employee.leaves = 20  # class variables can't be changed via object, It can be changed via class only 

#print(rohan.leaves)
#print(aalam.leaves)

'''rohan.name = "Rohan"
rohan.lname = "Singh"
rohan.salary = 444

aalam.name = "Aalam"
aalam.lname = "Rana"
aalam.salary = 555'''

print(rohan.salary, aalam.name)
