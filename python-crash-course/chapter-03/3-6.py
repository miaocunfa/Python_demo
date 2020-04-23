invitee = ["zhanan", 'zhanv', "zhazha"]
message = 'Can you come to dinner with me, '

print(invitee)
print(message + invitee[0])
print(message + invitee[1])
print(message + invitee[2])
print("")

print("i found a bigger table")

invitee.insert(0, '1')
print(invitee)
print(message + invitee[0])

invitee.insert(2, '2')
print(invitee)
print(message + invitee[2])

invitee.append('3')
print(invitee)
print(message + invitee[-1])
