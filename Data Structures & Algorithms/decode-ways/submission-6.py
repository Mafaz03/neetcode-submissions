class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = {}

        # def backtrack(idx):
        #     if idx in dp:
        #         # print("hit ", idx)
        #         return dp[idx]

        #     if idx == len(s):
        #         return 1
            
        #     if s[idx] == "0":
        #         return 0
            
        #     ways = backtrack(idx+1)
            
            
        #     if idx + 1 < len(s) and int(s[idx] + s[idx+1]) <= 26:
        #         ways += backtrack(idx+2)
                
        #     dp[idx] = ways
        #     return ways


        # return backtrack(0)

        dp = [0] * (len(s)+1)

        dp[len(s)] = 1

        for i in range(len(s)-1,-1,-1):
            print(i)
            
            if s[i] == "0":
                dp[i] = 0
                continue
            
            dp[i] = dp[i + 1]

            if i + 1 < len(s) and int(s[i] + s[i+1]) <= 26:
                dp[i] += dp[i+2]
                # dp[i] += 1

        return dp[0]