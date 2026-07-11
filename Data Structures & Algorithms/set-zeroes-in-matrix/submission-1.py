class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # mark row to be 0ed out
                    matrix[0][j] = 0 # mark col to be 0ed out

        for i in range(1, rows):
            for j in range(1, cols):
                if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                    matrix[i][j] = 0
        
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        if first_row_zero:
            matrix[0] = [0] * cols
        
        
        