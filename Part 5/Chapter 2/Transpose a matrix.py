def transpose(matrix: list) -> list :
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix


if __name__ == "__main__":
    matrix_notTranspose = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_transpose = transpose(matrix_notTranspose)
    print(matrix_transpose)