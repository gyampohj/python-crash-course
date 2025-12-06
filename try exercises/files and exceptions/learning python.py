from pathlib import Path

path = Path('learning_python.txt')

"""accessing the contents of a file"""
contents = path.read_text()
print(contents)


