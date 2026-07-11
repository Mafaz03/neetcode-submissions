class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for i in range(m)]
        dp[-1][-1] = 1

        for r in reversed(range(0,m)):
            for c in reversed(range(0,n)):
                if (r == m-1) and (c == n-1): 
                    print("no")
                    continue
                print(r,c)
                d = 0 if r == m - 1 else dp[r+1][c]
                ri = 0 if c == n - 1 else dp[r][c+1]
                dp[r][c] = d + ri

        return dp[0][0]