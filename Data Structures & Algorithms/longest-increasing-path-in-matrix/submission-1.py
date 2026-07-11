class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {} # {(i,j): path_len}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(i, j):

            if (i,j) in cache:
                # print("meow")
                return cache[(i,j)]

            path_len = 1
            for i_off, j_off in ([1,0], [0,1], [-1,0], [0,-1]):
                i_new = i + i_off
                j_new = j + j_off

                if (0 <= i_new < rows) and (0 <= j_new < cols):
                    if matrix[i_new][j_new] > matrix[i][j]: # only return when not favourable
                        path_len = max(path_len, 1 + dfs(i_new, j_new))

            cache[(i,j)] = path_len
            return path_len

        res = 1
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))

        return res