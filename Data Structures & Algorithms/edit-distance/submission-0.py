class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        k = len(word2)
        for i in range(len(word2)):
            temp = []

            for j in range(len(word1)+1):
                if j == len(word1):
                    temp.append(k)
                    k -= 1
                else:
                    temp.append(0)
            dp.append(temp)

        dp.append([i for i in reversed(range(len(word1)+1))])
        
        
        # print(dp)

        for i in reversed(range(len(word2))):
            for j in reversed(range(len(word1))):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                                        dp[i+1][j+1], # replace
                                        dp[i+1][j],   # delete
                                        dp[i][j+1]    # insert
                                    )
        # print(dp)
        return dp[0][0]










