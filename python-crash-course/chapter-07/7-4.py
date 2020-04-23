prompt = "\nPlease enter the ingredients of pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True

while active:
    ingredients = raw_input(prompt)

    if ingredients == 'quit':
        active = False
    else:
        print("We'll add " + ingredients.title() + " to pizza!")
