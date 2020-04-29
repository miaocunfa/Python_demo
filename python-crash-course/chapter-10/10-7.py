def addition(first_num, seconde_num):
    return first_num + seconde_num

def get_number(prompt):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except ValueError:
            print("please enter a number")
        else:
            return number

print("Give me two numbers, and I'll addition them.")

first_num = get_number('First number: ')
second_num = get_number('Second number: ')

addition_result = addition(first_num, second_num)
print("addition result: " + str(addition_result))
