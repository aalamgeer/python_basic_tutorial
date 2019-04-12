class activity:
	def walk(self):
		print("walk")
		
class dog(activity):
	def color(self, clr):
		print("%s This is dog color", clr)
	
class cat(activity):
	def color(self, clr):
		print("%s This is cat's color",clr)
	
dog1 = dog()
dog1.walk()
cat1 = cat()
cat1.walk()
	