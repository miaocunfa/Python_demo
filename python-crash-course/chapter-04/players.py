players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("original:")
print(players)

print("\nplayers[0:3] ")
print(players[0:3])

print("\nplayers[1:4] ")
print(players[1:4])

print("\nplayers[:4] ")
print(players[:4])

print("\nplayers[2:] ")
print(players[2:])

print("\nplayers[-3:] ")
print(players[-3:])

print("\nHere are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
