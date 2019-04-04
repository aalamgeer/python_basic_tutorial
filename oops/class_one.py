class Point:
	def draw(self):
		print("Draw")
	def move(self):
		print("move")


obj1 = Point()
obj2 = Point()
print (obj1.draw(), obj2.move())

obj1.x = 10
obj1.y = 20

print(obj1.x)
obj1.x = 25
print(obj1.x)