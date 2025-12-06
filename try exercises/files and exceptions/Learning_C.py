from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

""""replacing a word in a string"""
lines = contents.splitlines()
for line in lines:
    print(line.replace('Python', 'C'))