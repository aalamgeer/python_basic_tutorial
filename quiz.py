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
    print(f"You are {wg} pounds")
elif unit == 'l':
    wg = wg*0.45
    print(f"You are: {wg} Kilo Grams")

# Guess number
guessno = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    no = int(input("Enter the guess number:"))
    if no == guessno:
        print('You win')
        break
    guess_count += 1
else:
    print("you lose")