#lambda function can have any numbers of parameter and only one expression

g = lambda x: x*x*x
print(g(2))

#lambda with filter function, Filter takes a list as an argument and filter whole list as you want.
alist = [1,2,3,4,5,6,7,8,9,10,11]
#Find the all odd value's list from alist
filter_list = list(filter(lambda x:x%2 != 0, alist))
print(filter_list)

#Find even no. from list
find_even = list(filter(lambda x: x%2 == 0, alist)) 
print(find_even)


#map function->> map function takes two arguments first is function second is list
#This used with lambda function. It change each element of given list and lambda defination.
multiply_list_by_2 = list(map(lambda x: x*2, alist))
print(multiply_list_by_2)

#Reduce function -> Used to redunce list item Or make sum of whole numeric list.
from functools import reduce 
redunced_list = reduce(lambda x, y: x+y, alist)
print(redunced_list)
