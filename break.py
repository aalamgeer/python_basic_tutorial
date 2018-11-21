for x in range(2,10):
	for n in range(2,x):
		if x % n == 0:
			print x, 'is equal ',n ,'*', x/n
			break
	else:
		print x," Is prime number"