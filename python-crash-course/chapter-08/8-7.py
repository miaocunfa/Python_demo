def make_album(singer,album,num=''):
    albums = {'singer': singer, 'album': album}
    if num:
        albums['num'] = num
    return albums

print(make_album('sunyanzi','tianheihei'))
print(make_album('sunyanzi','kebule','10'))
print(make_album('meimei','Love Story'))
