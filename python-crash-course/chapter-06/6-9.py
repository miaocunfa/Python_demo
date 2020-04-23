favorite_places = {
    "zhanan":['dalian','shenyang','jinan'],
    "zhazha":['dalian','tianjin'],
    "zhagod":['jinan'],
    }

for name,places in favorite_places.items():
    print(name + "'s favorite places are:")
    for place in places:
        print("\t" + place)
    print("")
