people = {
    'Jane' : {
    'first_name': 'Jane',
    'last_name' : 'Holmes',
    'age' : 35,
    'city': 'Manchester'},

    'Justice' : {
        'first_name' : 'Justice',
        'last_name' : 'Gyampoh',
        'age' : 22,
        'city': 'Accra'
    },

    'Adelaide' : {
        'first_name': 'Adelaide',
        'last_name': 'Hunter',
        'age': 30,
        'city' : 'Sydney'
    }
}

#To print every info about the person
for person in people:
    for k, v  in people.items():
        print(f"{k.title()} : \n{v}")
