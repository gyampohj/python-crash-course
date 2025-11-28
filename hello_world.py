#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


#example
pizza = ['bbq', 'chicken deluxe', 'mozarellla', 'sausage and ham']
examples = pizza[:]
for pizza in pizza:
    print(f"I like {pizza} pizza")
print("I like it baked fresh and hot \nI really love pizza!") 

print(f"The first 3 items on my list are {examples}")