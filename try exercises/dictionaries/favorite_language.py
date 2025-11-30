favorite_language = {
    'jay' : 'rust',
    'john' : 'ruby',
    'jake': 'python'
}
poll = ['jay','jack','john','jude']

for person in poll:
    if person in favorite_language:
        print(f"Thanks for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take the polls")