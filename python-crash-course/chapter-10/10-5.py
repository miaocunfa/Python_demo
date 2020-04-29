filename = 'reason.txt'

prompt = '\nWhy do you like programming?\n'
prompt += "(Enter the 'q' to quit!) "

active = True

while active:
    reason = input(prompt)
    
    if reason == 'q':
        active = False
    else:
       with open(filename, 'a') as file_object:
           file_object.write(reason + "\n")
