import random 

print random.randint(0,10)  # randint return random integer within range

print random.random()* 100

# choose random number from a list
mylist = [2,3,8,7,"Aalam",1.2,52.6]
print random.choice(mylist)

# Generate list from random
my_list = []
for i in range(10):
	my_list.append(random.randrange(1,100,1))
print my_list

#another method
new_list = [random.randint(1,50) for x in range(1,10)] 
print new_list