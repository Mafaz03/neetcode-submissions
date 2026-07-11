class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        matrix.reverse()
        
        for i in range(rows):
            for j in range(i+1, cols):
                print(matrix[j][i], end = " ")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        