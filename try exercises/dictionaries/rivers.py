rivers =  {
    'nile' : 'egypt',
    'thames' : 'london',
    'volta' : 'ghana'
 }


#sentence  about each river
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

#names of rivers
print("\nRivers:")
for river in rivers.keys():
    print(f"{river.title()}")

#names of countries
print("\nCountries")
for country in rivers.values():
    print(country.title())

