#adding values to dict
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Empty string 
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)#

for username, user_info in users.items():

    print(f"\nUsername: {username}")

full_name = f"{user_info['first']} {user_info['last']}"
location = user_info['location']

print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {location.title()}")