import re
pattern = "Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print ("Match")
else:
    print ("Not match")