import re
text = "Hello Aalamgeer"
x = re.search('^Hr$',text)  #search retrun only first match object if more than one found
if(x):
	print(x)
else:
	print(x)
	
txt2 = "The rain in spain"
a = re.findall('ai', txt2)  # findall Return a list of matched string
print(a)

str = "The rain in spain"  # split method return a list where the string split on each match 
b = re.split('\s', str)		# Here match is whitespace (\s)
print(b)					#You can control the number of occurrences by specifying the maxsplit parameter:

str = "The rain in spain"  
b = re.split('\s', str, 1)		#You can control the number of occurrences by specifying the maxsplit parameter:
print(b)					

str = "The rain in spain"	# sub method used to replace match with your choice text
c = re.sub('\s'," RANA ",str)
print(c)

str = "The rain in spain"	# You can control the number of replacements by specifying the count parameter:
c = re.sub('\s'," RANA ",str, 1)
print(c)