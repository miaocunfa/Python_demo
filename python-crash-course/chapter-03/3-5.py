invitee = ["zhanan", 'zhanv', "zhazha"]
message = 'Can you come to dinner with me, '

print(message + invitee[1])
print(message + invitee[2])
print("")

invitee_not = "zhanan"
invitee[0] = "zhadi"

print(invitee_not + " Unable to keep the appointment!")
print(message + invitee[0])
