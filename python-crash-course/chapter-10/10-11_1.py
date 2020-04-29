import json

favorite_num = input("What is your favorite num? ")
    
filename = 'favorite_num.json'
with open(filename, 'w') as file_objects:
    json.dump(favorite_num, file_objects)
    print("We'll remember your favorite_num! " + favorite_num)

