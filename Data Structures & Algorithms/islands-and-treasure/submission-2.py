class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        dq = deque([])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dq.append((i,j,0))

        visited = set()


        while dq:
            r, c, dis = dq.popleft()
            grid[r][c] = dis
            visited.add((r,c))

            for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                row = r + r_off
                col = c + c_off

                if (0 <= row < rows) and (0 <= col < cols) and ((row,col) not in visited) and (grid[row][col] == 2147483647):
                    dq.append((row, col, dis+1))
                    visited.add((row, col))
