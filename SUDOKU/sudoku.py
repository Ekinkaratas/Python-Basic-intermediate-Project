def print_grid (sukodu : list) :
    for row in sudoku :
        for element in row :
            if element >= 0 :
                print(f" {element}" , end=' ')
            else:
                print(" _", end="")
        print()

def row_correct(sudoku: list, row_no: int) :
    row = sudoku[row_no]

    for element in row :
        if element > 0  and row.count(element) > 1:
            return False
        
    return True

def column_correct(sudoku: list, column_no: int):
    for row in sudoku:
        element = row[column_no]  # Get the element in the given column
        if element > 0 and row.count(element) == 1:  # Ignore 0s (empty cells)
                 return True
        
    return False

def small_matrix_correct(sudoku: list, i , j) :
    small_matrix = []
    for i in range(i,i+3) :
        for j in range(j,j+3) :
            small_matrix.append(sudoku[i][j])

    small_matrix_control = True 
    for var in small_matrix :
        if small_matrix.count(var) >0 and var>0 :
            small_matrix_control = False 
            break

    return small_matrix_control

def sudoku_grid_correct( sudoku:list ) :
    # Row Control and Column Control
    for i in range(len(sudoku)):
       if row_correct(sudoku, i) == False  or column_correct(sudoku, i) == False :
           return False
    

    # Column Control
    #for i in range(len(sudoku)) :
    #    if  column_correct(sudoku, i) == False :
    #        return False

    # 3X3 Matris Control
    for i in range(0,7,3) :
        for j in range(0,7,3) :
           if small_matrix_correct(sudoku,i,j) == False :
               return False
    return True



sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))