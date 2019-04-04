class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		print(f"x : {x}")
		print(f"y : {y}")
	def draw(self):
		print("Draw")
	def move(self):
		print("move")


obj1 = Point(10,20)

#Exercise of person class
class person:
	def __init__(self,name):
		self.name = name
		
	def talk(self):
		return (f"Hi i am {self.name}")
		
me = person("Aalam Geer Rana")
print(me.name)
print(me.talk())