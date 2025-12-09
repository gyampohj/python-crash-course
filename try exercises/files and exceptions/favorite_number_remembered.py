from pathlib import Path 
import json

path = Path('numbers.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("Enter your favorite number:")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thank you, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")