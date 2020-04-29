def show_magicians(magicians):
    for magician in magicians:
        print("Hello, " + magician + "!") 

def make_great(magicians):
    new_magicians = []
    for magician in magicians:
        new_magician = "the Great magician " + magician
        new_magicians.append(new_magician)
    return new_magicians

magicians = ['liuqian', 'dawei', 'zhanan']
new_magicians = make_great(magicians[:])

show_magicians(magicians)
print("")
show_magicians(new_magicians)
