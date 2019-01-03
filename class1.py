class Employee:
	leaves = 10
	
aalam = Employee()
rohan = Employee()

Employee.leaves = 20

print(rohan.leaves)
print(aalam.leaves)
