list = [value for value in range(1,10)]

for i in list:
    if i == 1:
        print(str(i) + "st")
    elif i == 2:
        print(str(i) + "nd")
    elif i == 3:
        print(str(i) + "rd")
    elif i > 3:
        print(str(i) + "th")
