while True:
    topping = input("Enter a pizza topping  (or 'quit' to stop): ")

    if topping.lower() == 'quit':
        break
    print(f"I will add {topping} to your pizza")