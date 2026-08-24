class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1: return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])


        dp = [[0]*cols for i in range(rows)]
        dp[0][0] = 1

        for r in range(rows):
            for c in range(cols):
                r_ = r - 1
                c_ = c - 1

                if obstacleGrid[r][c] != 1:
                    

                    if r_ >= 0:
                        dp[r][c] += dp[r_][c]
                    
                    if c_ >= 0:
                        dp[r][c] += dp[r][c_]
                else:
                    dp[r][c] = 0
        return dp[-1][-1]


        