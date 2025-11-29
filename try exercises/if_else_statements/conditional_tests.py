car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#equality and inequality with strings
#equality
preferred_fish = "tilapia"
if preferred_fish ==  "tilapia":
    print("I want it grilled!")

#inequality
preferred_fish = "Tuna"
if preferred_fish !=  "tilapia":
    print("I want it grilled!")


#Numerical tests
age = 23
if age == 23:
    print('You are an adult')

#list check
my_friends  = ['Feli', 'Ana', 'Mary', 'Hiba']
colleague = 'Ellie'
if colleague not in my_friends:
    print(f"{colleague.title()} is not my friend.")