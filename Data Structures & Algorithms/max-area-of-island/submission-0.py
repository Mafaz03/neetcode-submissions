class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set() # {(r, c)}
        
        def bfs(r, c):
            area = 1
            dq = deque([(r, c)])
            visited.add((r, c))

            while dq:
                r, c = dq.popleft()

                for (r_off, c_off) in [(0,1), (1,0), (0,-1), (-1,0)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols):
                        if grid[row][col] == 1 and (row, col) not in visited:
                            dq.append((row, col))
                            visited.add((row, col))
                            area += 1
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(bfs(i, j), max_area)
    
        return max_area


        