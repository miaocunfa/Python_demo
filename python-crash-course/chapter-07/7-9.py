sandwich_orders = ['meat', 'pastrami', 'pastrami', 'tomato', 'pastrami', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    finish = sandwich_orders.pop()
    
    if finish == 'pastrami':
        print("Sorry, pastrami sandwich sold out!")
    else:
        finished_sandwiches.append(finish)
        print("I made your " + finish + " sandwich")

print("\nAll sandwiches are made:")
for i in finished_sandwiches:
    print("\t" + i.title())
