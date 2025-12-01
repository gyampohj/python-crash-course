sandwich_orders = ['club', 'pastrami', 'tuna', 'cuban', 'veg']
finshed_sandwich = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    sandwich_orders.remove('tuna')

for sandwich in sandwich_orders:
    print(f"I made you a {sandwich} sandwich.")
    finshed_sandwich.append(sandwich)

print("\nThe following sandwiches were made")
for sandwich in finshed_sandwich:
    print(f"- {sandwich} sandwich")