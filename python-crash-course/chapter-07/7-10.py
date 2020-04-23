prompt = "\nIf you could visit one place in the world,"
prompt += "where would you go?"
prompt += "\n(Enter 'quit' when you are finished.) "

dream_travel = []
active = True

while active:
    place = raw_input(prompt)
    
    if place != 'quit':
        dream_travel.append(place)
    else:
        break

if dream_travel:
    print("")
    for place in dream_travel:
        print(place)
else:
    print("\nYou haven't said where you're going!")
