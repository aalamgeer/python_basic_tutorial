import re
pattern = r"Cookie"  # r is called raw string used for handle special chrater or backslashes
sequence = "Cookie"
if re.match(pattern, sequence):  #Match function return a object if text match otherwise none
    print ("Match")
else:
    print ("Not match")

# Wild card character . dot is most used special charater (A period matches any single charater except new line)

print(re.search(r'C.ok.e', 'Cookie').group()) # output will be cookie

# \w small w use to match any single charater single digit or underscore
match = re.search(r'A\wlam\weer', 'AalamGeer').group()
print (match)

# \W capital w use to matches any charater not part of small \w
match = re.search(r'C\Wke', 'C@ke').group()
print(match)

# \s use to matches a single whitespace in string
match = re.search('I\sam\sa\sboy', 'I am a boy').group()
print(match)

# \t use to matches any tab in string
#match = re.search(r'are\tsame', 'are  same').group()
#print(match)

# \d use to matches digit  0-9
match = re.search(r'Co\de\sis\s\d\d\d%\slife','Co9e is 100% life').group()
print(match)

# ^ use for start with any character start with
match = re.search(r'^Eat', 'Eat here').group()
print(match)

# $ use for the ends with any charater
match = re.search(r'Aalam Geer Rana$', 'Aalam Geer Rana').group()
print(match)

#[] use to set range [a-z0-9]
match = re.search(r'[0-9]s+','4s').group()
print(match)

# \A match only at the strting of the string
match = re.search(r'\A[A-D]ookie', 'Cookie').group()
print(match)

# Repetations ############################
# + operator check one or more repete charaters to its left side
match = re.search(r'Co+kie', 'Cooooookie').group()
print(match)

# * Operator check zero or one repeat charater to its left
match = re.search(r'Co*kie','Ckie').group()
print(match)