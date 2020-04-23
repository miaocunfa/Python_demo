tom = {'name':'tom', 'type':'cat', 'master':'jerry'}
xiaotian = {'name':'xiaotian', 'type':'dog', 'master':'yangjian'}
bajie = {'name':'bajie', 'type':'pig', 'master':'tangtang'}

pets = [tom, xiaotian, bajie]

for pet in pets:
    print(pet['name'] + " is a " + pet['type'] + ", it owner " + pet['master'])
