filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content)

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)


