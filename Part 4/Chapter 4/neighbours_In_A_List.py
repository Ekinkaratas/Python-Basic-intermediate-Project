def longest_series_of_neighbours(my_list: list):
    max_series = 0
    longest_series = 1  

    for i in range(len(my_list) - 1):  
        if abs(my_list[i] - my_list[i + 1]) == 1:  
            longest_series += 1
        else:
            max_series = max(max_series, longest_series)  
            longest_series = 1 

    max_series = max(max_series, longest_series)  
    return max_series


my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))    