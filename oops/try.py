try:
	age = int(input("Age:"))
	print(age)
except ValueError:
	print("Not valid age")