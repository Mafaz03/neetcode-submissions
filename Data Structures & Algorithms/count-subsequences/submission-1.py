class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {} # {(i,j): ways}

        def dfs(i, j):

            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i,j) in cache:
                # print("meow")
                return cache[(i,j)]

            ways = 0

            if s[i] == t[j]:
                ways += (dfs(i+1, j) + dfs(i+1, j+1))
            else:
                ways += dfs(i+1, j)

            cache[(i,j)] = ways
            return ways

        return dfs(0, 0)