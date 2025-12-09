from pathlib import Path

def count_common_words(filename, word):
    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f" '{word}' appears in {filename} about {word_count} times"
        print(msg)

filename = 'common_words.txt' 
count_common_words(filename, '')