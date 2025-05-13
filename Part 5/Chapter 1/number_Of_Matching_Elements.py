def count_matching_elements(my_matrix: list, element: int) :
    sayac = 0

    for row in my_matrix :
        if element in row :
            sayac += row.count(element)
    
    return  sayac
    
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))