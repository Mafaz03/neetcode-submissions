class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        
        matrix_T = [[0] * rows for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                matrix_T[j][i] = matrix[i][j]
        return matrix_T