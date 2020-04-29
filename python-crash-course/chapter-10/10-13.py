import json

def get_stored_username():
    filename = "username.json"

    try:
        with open(filename) as file_objects:
            username = json.load(file_objects)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your username? ")
    filename = "username.json"
    with open(filename, 'w') as file_objects:
        json.dump(username, file_objects)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        answer = input(username + ", Is this your username(y/n)?")
        if answer == 'y' or answer == 'Y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
