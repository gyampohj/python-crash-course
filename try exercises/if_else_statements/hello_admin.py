#Hello Admin
username = ['Jaden', 'scholes', 'admin','holmes','jade']
for username in username:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")

#No users
if username == []:
    print("We need to find some users")
elif username != []:
    print("There are some users in the database")        