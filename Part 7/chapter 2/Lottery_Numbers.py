import random
def lottery_numbers(amount: int, lower: int, upper: int):
   list = [random.randint(lower,upper) for _ in range(amount)]
   return sorted(list)

new_List = lottery_numbers(7, 1, 40)

for var in new_List:
    print(f"{var} ",end='')
