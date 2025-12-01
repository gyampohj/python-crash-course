dream_vacations = {}

while True:
    destination = input("Where do you want to visit?")
    if destination.lower() == 'exit':
        break
    if destination in dream_vacations:
        dream_vacations[destination] += 1
    else:
        dream_vacations[destination] = 1

print("\nPoll Results")
for destination, count in dream_vacations.items():
    print(f"{destination}: {count} votes(s)")