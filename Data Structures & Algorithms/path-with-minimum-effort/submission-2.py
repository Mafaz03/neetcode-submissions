class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [] # (abs difference, (x,y))

        rows = len(heights)
        cols = len(heights[0])

        if rows == 1 and cols == 1: return 0

        if cols > 1: heapq.heappush(heap, (abs(heights[0][0] - heights[0][1]), (0,1)))
        if rows > 1: heapq.heappush(heap, (abs(heights[0][0] - heights[1][0]), (1,0)))

        max_value = float("-inf")

        visited = set()

        while heap:
            cost, (x,y) = heapq.heappop(heap)
            max_value = max(max_value, cost)

            if (x,y) in visited: continue
            visited.add((x,y))

            if (x == rows-1) and (y == cols-1): break

            for (x1, y1) in [(0,1), (1,0), (-1,0), (0, -1)]:
                x_new = x1 + x
                y_new = y1 + y

                if (0 <= x_new < rows) and (0 <= y_new < cols):
                    heapq.heappush(heap, (abs(heights[x][y] - heights[x_new][y_new]), (x_new, y_new)))

        return max_value
                    




