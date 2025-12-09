from pathlib import Path 
import json

favourite_number = input("Enter your favourite number: ")

path = Path('numbers.json')
contents = json.dumps(favourite_number)
path.write_text(contents)

print("I'll remember this number")



from pathlib import Path 
import json


path = Path('numbers.json')
contents = path.read_text()
favourite_number = json.loads(contents)

print(f"I know your favourite number! It's {favourite_number}")
