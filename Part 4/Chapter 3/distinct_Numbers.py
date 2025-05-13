def distinct_numbers (array : list):
    # Solution 1
    return list(set(array))
    # Solution 2
    #return list(dict.fromkeys(array))


my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))