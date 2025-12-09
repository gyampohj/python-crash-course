print("Enter 'q' to quit the program at any time")

while True:
    try:
        x = input("Provide a number:")
        if x == 'q':
            break

        x = int(x)

        y= input("Provide another number:") 
        if y == 'q':
            break

        y = int(y)


    except ValueError:
        print("Sorry, please input a number")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}")
