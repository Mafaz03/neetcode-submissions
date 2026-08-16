class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]

        dp[0] = True

        # find the next True idx
        for i in range(n):
            if (s[i] == "0") and dp[i] == True:
                for j in range(i + minJump, min(i + maxJump + 1, n)):
                    if s[j] == '0':
                        dp[j] = True

        print(dp)
        return dp[-1]

