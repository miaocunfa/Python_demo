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
print("")

invitee.insert(2, '2')
print(invitee)
print(message + invitee[2])
print("")

invitee.append('3')
print(invitee)
print(message + invitee[-1])
print("")

print("i'm sorry, Because the table couldn't be delivered in time, I can only invite two people")

pop_invitee=invitee.pop()
message2="Sorry, I'll invite you next time. "
print(message2 + pop_invitee)
print(invitee)

pop_invitee=invitee.pop()
print(message2 + pop_invitee)
print(invitee)

pop_invitee=invitee.pop()
print(message2 + pop_invitee)
print(invitee)

pop_invitee=invitee.pop()
print(message2 + pop_invitee)
print(invitee)

print(message + invitee[-1])
print(message + invitee[-2])
