class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0],(0,0))]

        res = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            r, c = n1

            if n1 in visited:
                continue
            
            visited.add(n1)

            res = max(res, w1)
            
            if n1 == (rows-1, cols-1): break

            for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r_new, c_new = r + r_off, c + c_off
                if (0 <= r_new < rows) and (0 <= c_new < cols):
                    if (r_new, c_new) not in visited:
                        heapq.heappush(min_heap, (grid[r_new][c_new], (r_new, c_new)))
        return res