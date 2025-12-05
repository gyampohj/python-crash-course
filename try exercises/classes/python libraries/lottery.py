import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 'A', 'B', 'C', 'D', 'E']
winning_selection = random.sample(lottery_pool, 4)
print(f"Any ticket matching these 4 letters or numbers win: {winning_selection}")