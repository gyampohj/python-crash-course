from pathlib import Path

name = input("Enter your name :")
Path('guest.txt').write_text(name)