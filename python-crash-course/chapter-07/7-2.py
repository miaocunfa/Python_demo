message = raw_input("How many of you?")
message = int(message)

if message > 8:
    print("I'm sorry, there's no empty table")
else:
    print("We still have a free table")
