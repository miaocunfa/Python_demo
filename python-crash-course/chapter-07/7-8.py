sandwich_orders = ['meat', 'tomato', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    finish = sandwich_orders.pop()
    finished_sandwiches.append(finish)
    print("I made your " + finish + "sandwich")

print("\nAll sandwiches are made:")
for i in finished_sandwiches:
    print("\t" + i.title())
