#lambda function can have any numbers of parameter and only one expression

g = lambda x: x*x*x
print(g(2))

#lambda with filter function, Filter takes a list as an argument and filter whole list as you want.
alist = [1,2,3,4,5,6,7,8,9,10,11]
#Find the all odd value's list from alist
filter_list = list(filter(lambda x:x%2 != 0, alist))
print(filter_list)
