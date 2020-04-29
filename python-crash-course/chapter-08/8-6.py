def city_country(city, country):
    city_country = '"' +  city.title() + ", " + country.title() + '"'
    return city_country

print(city_country('dalian','china'))
print(city_country('lanzhou','china'))
print(city_country('london','england'))
