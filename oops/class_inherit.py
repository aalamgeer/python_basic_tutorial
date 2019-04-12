class activity:
	def walk(self):
		print("walk")
	def color(self, clr):
		print(f"{clr} This is dog color")
		
class dog(activity):
	pass
	
class cat(activity):
	pass
	
dog1 = dog()
dog1.walk()
cat1 = cat()
cat1.walk()
dog1.color("Black")
cat1.color("White")	