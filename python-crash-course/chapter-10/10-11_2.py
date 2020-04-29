import json

filename = 'favorite_num.json'

with open(filename) as file_objects:
    favorite_num = json.load(file_objects)
    print("Your favorite num is " + favorite_num)
