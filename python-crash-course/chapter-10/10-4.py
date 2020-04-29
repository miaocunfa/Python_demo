filename = 'guest_book.txt'

prompt = '\nPlease input your name\n'
prompt += "(Enter the 'q' to quit!) "

active = True

while active:
    username = input(prompt)
    
    if username == 'q':
        active = False
    else:
       with open(filename, 'a') as file_object:
           file_object.write(username + "\n")
