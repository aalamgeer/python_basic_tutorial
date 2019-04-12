class activity:
	def walk(self):
		print("walk")
		
class dog(activity):
	def color(self, clr):
		print(f"{clr} This is dog color")
	
class cat(activity):
	def color(self, clr):
		print(f"{clr} This is cat's color")
	
dog1 = dog()
dog1.walk()
cat1 = cat()
cat1.walk()
dog1.color("Black")
cat1.color("White")	