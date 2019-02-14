#----- Join method is used to join all elements of list or tuple or dict--
mylist = ['Apple', 'Banana', 'Orange']
mytup = ('Lion', 'Cat', 'Dog')
myDict = {"name": "John", "country": "Norway"} # ----------- When dict via join then only key will join in string
mystr = " ".join(mylist)
mystr2 = " ".join(mytup)
mystr3 = " ".join(myDict)
print mystr
print mystr2
print mystr3
