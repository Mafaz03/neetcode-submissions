class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        heap = []

        rows = len(grid)
        cols = len(grid[0])

        if (rows == 1) and (cols == 1):
            return grid[0][0]

        top_left = grid[0][0]

        if cols > 1: heapq.heappush(heap, (top_left + grid[0][1], (0,1)))
        if rows > 1: heapq.heappush(heap, (top_left + grid[1][0], (1,0)))
        
        visited = set()

        while heap:
            min_sum, (x, y) = heapq.heappop(heap)

            if (x, y) == (rows-1, cols-1):
                return min_sum

            if (x, y) in visited:
                continue

            visited.add((x, y))
            
            if x + 1 < rows: 
                heapq.heappush(heap, (min_sum + grid[x+1][y], (x+1,y)))
        
            if y + 1 < cols: 
                heapq.heappush(heap, (min_sum + grid[x][y+1], (x,y+1)))
            