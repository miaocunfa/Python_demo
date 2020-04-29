def show_magicians(magicians):
    for magician in magicians:
        print("Hello, " + magician + "!") 

def make_great(magicians):
    for i in range(0,len(magicians),1):
        magicians[i] = "the Great magician " + magicians[i]

magicians = ['liuqian', 'dawei', 'zhanan']
make_great(magicians)
show_magicians(magicians)
