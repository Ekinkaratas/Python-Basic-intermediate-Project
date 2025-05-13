def length_of_longest ( my_list ) :
    longest_word = " "
    for var in my_list:
        if len(longest_word) < len(var) :
            longest_word = var
    
    return longest_word


my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(len(result))

