class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        

        dq = deque([])
        visited = set()

        not_rotten = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dq.append((i,j))
                if grid[i][j] == 1:
                    not_rotten += 1
        if not_rotten == 0: return 0

        time = -1

        while dq:
            time += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()

                for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols) and ((row,col) not in visited) and (grid[row][col] == 1):
                        grid[row][col] = 2
                        dq.append((row, col))
                        visited.add((row, col))
                        
                        not_rotten -= 1
                        
        return time if not_rotten == 0 else -1