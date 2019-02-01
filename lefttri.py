for i in range(0,5):
    for n in range(0,i):
        print ("*", end = "")
		
# Another way
print '\n'.join(['*' * (row+1) for row in range(7) ])
   
