try:
	age = int(input("Age:"))
	income = 20000
	risk = income / age
	print(risk)
except ZeroDivisionError:
	print("Age con not be zero")
except ValueError:
	print("Not valid age")