cities = {
    'dalian':{
        'country':'china',
        'population':595.2,
        'fact':'First-tier City',
        },

    'beijing':{
        'country':'china',
        'population':2153.6,
        'fact':'First-tier City',
        },

    'lanzhou':{
        'country':'china',
        'population':375.36,
        'fact':'Second-tier City',
        },
    }

for city, city_info in cities.items():
    print("City: " + city)
    print("Country: " + city_info['country'])
    print("Population: " + str(city_info['population']))
    print("Fact: " + city_info['fact'] + "\n")
