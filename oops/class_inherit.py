class activity:
	def walk(self):
		print("walk")
		
class dog(activity):
	pass
	
class cat(activity):
	pass
	
dog1 = dog()
dog1.walk()
cat1 = cat()
cat1.walk()
	