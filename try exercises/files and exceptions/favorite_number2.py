from pathlib import Path 
import json


path = Path('numbers.json')
contents = path.read_text()
favourite_number = json.loads(contents)

print("I know your favourite number! It's {favourite_number}")
