try:
    x = input("Provide a number:")
    x = int(x)

    y= input("Provide another number:") 
    y = int(y)
except ValueError:
    print("Sorry, please input a number")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}")
