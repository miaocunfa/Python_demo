friends_num = {
    'zhazha':['8', '13'], 
    'zhanv': ['6', '8'], 
    'zhanan':['3', '6', '9'], 
    'zhagod':['6', '8', '1995'], 
    'zhadi': ['7'],
    }

for name,nums in friends_num.items():
    print(name + "'s favorite nums are:")
    for num in nums:
        print("\t" + num)
    print("")
