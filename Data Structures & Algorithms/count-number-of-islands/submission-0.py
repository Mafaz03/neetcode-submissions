class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set() # {(r, c)}

        def bfs(r, c):
            dq = deque([(r, c)])
            visited.add((r, c))

            while dq:
                r, c = dq.popleft()

                for (r_off, c_off) in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if (0 <= r + r_off < rows) and (0 <= c + c_off < cols):
                        if grid[r + r_off][c + c_off] == "1" and (r + r_off, c + c_off) not in visited:
                            dq.append((r + r_off, c + c_off))
                            visited.add((r + r_off, c + c_off))
                            

        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    
                    num_islands += 1
                    bfs(i, j)

        return num_islands
        