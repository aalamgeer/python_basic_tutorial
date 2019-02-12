string = raw_input ('Enter string')
rvs = string[::-1]
if string == rvs:
	print "The string in palindrome"
else:
	print "Not palindrome"
	
#--------------------------------------------------- another way below -----
if string[::] == string[::-1]:
	print "palindrome"
