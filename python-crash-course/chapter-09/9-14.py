from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

six = Die(6)
print("six sides: ")
for i in range(1, 11, 1):
    x = six.roll_die()
    print(str(x))

print("")

ten = Die(10)
print("ten sides: ")
for i in range(1, 11, 1):
    x = ten.roll_die()
    print(str(x))

print("")

twenty = Die(20)
print("twenty sides: ")
for i in range(1, 11, 1):
    x = twenty.roll_die()
    print(str(x))
