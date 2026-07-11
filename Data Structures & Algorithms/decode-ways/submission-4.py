class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def backtrack(idx):
            if idx in dp:
                # print("hit ", idx)
                return dp[idx]

            if idx == len(s):
                return 1
            
            if s[idx] == "0":
                return 0
            
            ways = backtrack(idx+1)
            
            
            if idx + 1 < len(s) and int(s[idx] + s[idx+1]) <= 26:
                ways += backtrack(idx+2)
                
            dp[idx] = ways
            return ways


        return backtrack(0)