#---------Read the file-----------
#a = open('sample.txt', 'r')

#print(a.readlines())   read all lines with '\n'

#print(a.read())   #read Full file line

#print(a.readline())    #read only first line

#for x in a:
#	print(x)

#---------Append content in file-----------

#b = open('sample.txt', 'a')   # use to open file in append mode
#b.write(" --Thanks this line is my signature")   # This text will append in file on each run.

#c = open('sample.txt', 'r')
#print(c.read())

#----------Write the current file (overwrite the data)-----------
#w = open('sample.txt', 'w')
#txt = "This new content added by the Aalamgeer using pytho file write method"
#w.write(txt)
f = open('sample.txt','r')
print(f.read())
