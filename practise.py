number = [5,2,5,2,2]
for itm in number:
	#print('*'*itm) simle technique, For this we can use nested loop
	for n in range(itm):
		print('*', end='')
	print()
	
# Find duplicate number in list
unique = []
for n in number:
	if n not in unique:
		unique.append(n)
print(unique)

#find maximum number from list
max =0
for n in number:
	if n > max:
		max = n
print(max)