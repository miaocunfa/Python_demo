aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':'5', 'speed':'slow'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
