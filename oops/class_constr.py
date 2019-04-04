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
