class TrieNode:
    def __init__(self):
        self.children = {} # {'a': TrieNode()}
        self.isLast   = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        words = set(dictionary)
        dp = {}
        
        def dfs(start_idx):
            if start_idx == len(s):
                return 0
            else:
                if start_idx in dp:
                    return dp[start_idx]
                
                # skip the word
                res = 1 + dfs(start_idx + 1)

                # use the word
                for j in range(start_idx, len(s)):
                    if s[start_idx : j+1] in words:
                        res = min(res, dfs(j+1))

                dp[start_idx] = res
                
            return res
        return dfs(0)
