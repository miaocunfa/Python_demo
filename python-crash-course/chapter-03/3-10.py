china_five_great_mountains = ['DongYueTaiShan', 'XiYueHuaShan', 'NanYueHengShan', 'BeiYueHengShan', 'ZhongYueSongShan']

print("the " + str(len(china_five_great_mountains)) + " Famous Mountains in China")
print('')
 
print("sorted lit")
print(sorted(china_five_great_mountains))
print('')

print("sorted reverse list")
print(sorted(china_five_great_mountains,reverse=True))
print('')

already_go=china_five_great_mountains.pop(1)

print("i have already to go the " + already_go)
print("So, The rest: ")
print(china_five_great_mountains)
