guest = ['Justice', 'Joe', 'Jade', 'Kiki']
message =f"I have sent a dinner invitation to {guest[0]}"
print(message)

decline = f"{guest[2]} will not be able to make it to dinner"
print(decline)

print(f"{guest[0]} ,I have found a bigger table")

guest.insert(0, 'Duke')
print(guest)

guest.insert(2, 'Mike')
print(guest)

guest.append('Stella')
print(guest)

final = f"I am inviting you to dinner {guest[-2]}.\nI can only invite 2 people to dinner"
print(final)



update = f"{guest[1]}, I am inviting {len(guest)} people"
print(update)

