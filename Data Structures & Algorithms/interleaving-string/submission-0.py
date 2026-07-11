class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        i = j = k = 0

        cache = {} # {(i,j,k): bool}

        def dfs(i, j, k):
            if (i == len(s1)) and (j == len(s2)) and (k == len(s3)):
                return True
            
            if (i,j,k) in cache:
                print("meow")
                return cache[(i,j,k)]
            
            ans = False

            if i < len(s1) and s1[i] == s3[k]:        
                ans = dfs(i+1, j, k+1)
                
            if j < len(s2) and s2[j] == s3[k]:
                ans = dfs(i, j+1, k+1)

            cache[(i,j,k)] = ans

            return ans
                
            
        return dfs(0,0,0)