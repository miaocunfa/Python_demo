filename = 'guest.txt'
username = input("please input your name: ")

with open(filename, 'w') as file_object:
    file_object.write(username + "\n")
