def openfile(filename):
    try:
        with open(filename) as file_objects:
            lines = file_objects.readlines()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        lines = []
    else:
        pass

    return lines

catfile = 'cats.txt'
dogfile = 'dogs.txt'

cats = openfile(catfile)
dogs = openfile(dogfile)

if cats: 
    print("cats:")
    for cat in cats:
        print(cat.strip())

if dogs:
    print("\ndogs:")
    for dog in dogs:
        print(dog.strip())
