# first test
lbs = int(input("Enter the wight in lbs: "))
kg = lbs * 0.45
print("The wight in KG: ", kg)

# second test
price = 1000000
credit = "good"
if credit == "good":
    downpayment = price*10/100
else:
    downpayment = price*20/100
print(f"Down payment: ${downpayment}")