class Point:
	def draw(self):
		print("Draw")
	def move(self):
		print("move")


obj1 = Point()
obj2 = Point()
print (obj1.draw(), obj2.move())