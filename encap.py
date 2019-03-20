class Employee:
	maxprice = 'class value'
	def __init__(self):
		self.maxprice = 900
		
	def sell(self):
		print(" Selling price {} ".format(self.maxprice))
		
	def setprice(self, newprice):
		self.maxprice = newprice
		
obj = Employee
obj.sell
obj.setprice(100)