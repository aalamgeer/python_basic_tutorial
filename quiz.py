# first test
lbs = int(input("Enter the weight in lbs: "))
kg = lbs * 0.45
print("The weight in KG: ", kg)

# second test
price = 1000000
credit = "good"
if credit == "good":
    downpayment = price*10/100
else:
    downpayment = price*20/100
print(f"Down payment: ${downpayment}")

# third exercise
wg = int(input("Weight: "))
unit = input("l (lbs) Or k (kg)")
if unit == 'k':
    wg = abs(wg/0.45)
    print("You are:", wg, "Pounds")
elif unit == 'l':
    wg = wg*0.45
    print("You are:", wg, "Kilo Grams")