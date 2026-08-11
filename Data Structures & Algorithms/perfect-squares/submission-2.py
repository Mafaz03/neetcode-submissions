class Solution:
    def numSquares(self, n: int) -> int:
        possible = []

        if n == 1: return 1

        for i in range(1, n):
            a = i * i
            if a > n:
                break
            possible.append(a)

        print(possible)

        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for i in range(n+1):
            for sq in possible:
                if i - sq >= 0:
                    dp[i] = min(dp[i], 1+dp[i-sq])
        
        res = dp[n]
        return res




