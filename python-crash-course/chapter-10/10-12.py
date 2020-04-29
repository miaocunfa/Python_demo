import json

def get_stored_num():
    filename = "favorite_num.json"

    try:
        with open(filename) as file_objects:
            favorite_num = json.load(file_objects)
    except FileNotFoundError:
        return None
    else:
        return favorite_num

def get_new_num():
    favorite_num = input("What is your favorite num? ")
    filename = "favorite_num.json"
    with open(filename, 'w') as file_objects:
        json.dump(favorite_num, file_objects)
    return favorite_num

def greet_user():
    favorite_num = get_stored_num()
    if favorite_num:
        print("Your favorite num is " + favorite_num)
    else:
        favorite_num = get_new_num()
        print("We'll remember your favorite num! " + favorite_num)

greet_user()
