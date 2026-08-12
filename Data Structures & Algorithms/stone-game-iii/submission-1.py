class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # mem = {}

        # def dfs(i: int): # we will return the difference

        #     if i >= len(stoneValue):
        #         return 0

        #     if i in mem:
        #         return mem[i]

        #     gain = 0
        #     ans = float("-inf")

        #     for X in range(3):
        #         if i + X >= len(stoneValue): break

        #         gain += stoneValue[i + X]
        #         ans = max(ans, gain - dfs(i + X + 1))

        #     mem[i] = ans

        #     return ans

        # r = dfs(0)
        # if r > 0:
        #     return "Alice"
        # elif r < 0:
        #     return "Bob"
        # else:
        #     return "Tie"

        n = len(stoneValue)
        dp = [0] * (n+3)

        for i in range(n-1, -1, -1):
            gain = 0
            dp[i] = float("-inf")

            for X in range(3):
                if i + X >= n: break
                gain += stoneValue[i + X]
                dp[i] = max(dp[i], gain - dp[i + X + 1])
        r = dp[0]

        if r > 0:
            return "Alice"
        elif r < 0:
            return "Bob"
        else:
            return "Tie"