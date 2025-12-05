import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Rolling a {self.sides}- sided die: {random.randint(1, self.sides)}")

#usage
die_6 = Dice()
die_10 = Dice(10)
die_20 = Dice(20)

for _ in range(6):
    die_6.roll_die()
    die_10.roll_die()
    die_20.roll_die()