prompt = "\nPlease enter tell me you age, I'll tell you the price:"
prompt += "\n(Enter '0' when you are finished.) "

active = True

while active:
    age = raw_input(prompt)
    age = int(age)

    if age == 0:
        active = False
        break
    elif age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15

    print("you price is " + str(price))
