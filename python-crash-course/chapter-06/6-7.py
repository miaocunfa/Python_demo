friends_0 = {'first_name':'zha', 'last_name':'zha', 'age':'30', 'city':'dalian'}
friends_1 = {'first_name':'nan', 'last_name':'zha', 'age':'22', 'city':'nanning'}
friends_2 = {'first_name':'god', 'last_name':'zha', 'age':'25', 'city':'jinan'}

people = [friends_0, friends_1, friends_2]

for friend in people:
    fullname = friend['last_name'] + friend['first_name']

    print("My friend is " + fullname + ".")
    print("He is " + friend['age'] + " years old.")
    print("He live in " + friend['city'] + ".\n")
