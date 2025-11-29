current_users = ['kwasi1', 'kofi2', 'kwame3','Ama99', 'mr502']
new_users = ['kwasi1','kofi2','mrs997','error1']

for new_users in current_users:
    print("You have to enter a new username")
if new_users not in current_users:
    print("This username is available")