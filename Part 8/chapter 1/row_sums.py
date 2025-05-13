def row_sums(matrix : list):
    for rows in matrix :
        total = 0;
        for i in range(len(rows)):
            total += rows[i]
        
        rows.append(total)

    return matrix

my_matrix = [[1, 2, 3], [3, 4 ,7]]
row_sums(my_matrix)
print(my_matrix)