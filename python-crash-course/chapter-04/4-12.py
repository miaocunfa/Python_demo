my_fruit = ['mongo', 'orange', 'apple']
friend_fruit = my_fruit[:]

my_fruit.append("banana")
friend_fruit.append("durian")

print("My favorite fruit list are:")
for i in my_fruit:
    print(i)

print("\nMy friend's favorite fruit list are:")
for i in friend_fruit:
    print(i)
