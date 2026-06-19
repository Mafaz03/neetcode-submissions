class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])


        def bfs(r, c):
            visited = set()
            dq = deque([(r,c, 0)])
            visited.add((r,c))
            
            while dq:
                r, c, dis = dq.popleft()
                # print(r, c, dis)
                grid[r][c] = min(grid[r][c], dis)

                for r_off, c_off in [(1,0), (0,-1), (-1,0), (0,1)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols) and (row, col) not in visited and grid[row][col] > dis + 1:
                        dq.append((row, col, dis+1))
                        visited.add((row, col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i,j)