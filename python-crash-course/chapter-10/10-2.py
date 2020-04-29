filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.strip()
    new_line = line.replace("Python","C")
    print(new_line)
