def add_numbers_to_list(numbers: list) -> list:

    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1]+1)
        add_numbers_to_list(numbers)

    return numbers

numbers = [1,3,4,5,10,11]
add_numbers_to_list(numbers)
print(numbers)
