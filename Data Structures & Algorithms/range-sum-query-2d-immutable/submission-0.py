class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        sumMatrix = [0] * (cols+1)
        sumMatrix = [sumMatrix.copy() for _ in range (rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                
                if i == 1:
                    sumMatrix[i][j] = matrix[i-1][j-1] + sumMatrix[i][j-1]
                else:
                    sumMatrix[i][j] = matrix[i-1][j-1] + sumMatrix[i][j-1] + sumMatrix[i-1][j] - sumMatrix[i-1][j-1]


        self.sumMatrix = sumMatrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMatrix[row2+1][col2+1] - self.sumMatrix[row1][col2+1] - self.sumMatrix[row2+1][col1] + self.sumMatrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)