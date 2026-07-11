class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if (j >= len(p)) and (i >= len(s)):
                return True
            
            if j >= len(p):
                return False

            
            ans = False

            match = (i < len(s)) and (s[i] == p[j] or p[j] == ".")

            if (j+1 < len(p)) and  (p[j+1] == "*"):
                ans = ((match and dfs(i+1, j)) or   # use * and duplicate s[i]
                    (dfs(i, j+2)))                # skip * and dont use any more
            
            elif match:
                ans = dfs(i+1, j+1)
            
            return ans

        return dfs(0,0)