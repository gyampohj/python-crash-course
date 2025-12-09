from pathlib import Path
import json


def get_stored_username(path):

    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    username = input("What is your name?:")
    age = input("Enter you age:")
    location = input("Enter your location:")
     
    user_dict = {
        'username': username,
        'age': age,
        'location': location
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict
    

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_dict = get_stored_username(path)

    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"You are {user_dict['age']} years old")
        print(f"You stay in {user_dict['location']}")
    else:
        user_dict = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_dict['username']}!")
    
greet_user()