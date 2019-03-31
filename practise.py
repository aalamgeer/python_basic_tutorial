number = [5,2,5,2,2]
for itm in number:
	#print('*'*itm) simle technique, For this we can use nested loop
	for n in range(itm):
		print('*', end='')
	print()