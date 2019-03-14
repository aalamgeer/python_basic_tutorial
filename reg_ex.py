import re
pattern = r"Cookie"  # r is called raw string used for handle special chrater or backslashes
sequence = "Cookie"
if re.match(pattern, sequence):  #Match function return a object if text match otherwise none
    print ("Match")
else:
    print ("Not match")

# Wild card character . dot is most used special charater (A period matches any single charater)