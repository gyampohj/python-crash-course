from pathlib import Path

text_files = ['cats.txt' , 'dogs.txt']

for text_file in text_files:
    print(f"\nReading file: {text_file}")

    path = Path(text_file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(" Sorry, I can't find that file.")
    else:
        print(contents)