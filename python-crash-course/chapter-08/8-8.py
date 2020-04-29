def make_album(singer,album,num=''):
    albums = {'singer': singer, 'album': album}
    if num:
        albums['num'] = num
    return albums

active = True

while active:
    print("\nPlease tell me you favorite album and singer?")
    print("(enter 'q' at any time to quit)")

    album = raw_input("album: ")
    if album == 'q':
        break

    singer = raw_input("singer: ")
    if singer == 'q':
        break
    
    albums = make_album(singer, album)
    print("")
    print(albums)
    
#print(make_album('sunyanzi','tianheihei'))
#print(make_album('sunyanzi','kebule','10'))
#print(make_album('meimei','Love Story'))
