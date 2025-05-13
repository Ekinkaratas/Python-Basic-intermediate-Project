def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if number > limit]


numbers = [1,65, 32, -6, 9, 11]
list_a = remove_smaller_than(numbers, 10)
print(list_a)

print(remove_smaller_than([-4, 7, 8, -100], 0))