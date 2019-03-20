a, b = 0, 1
while b < 10:
   print (b)
   a, b = b, a+b

# pound to kilogram convertion
wightpound = int(input('Enter wight in pounds: '))
kg = wightpound/2.2046
print(kg, 'Kilograms')