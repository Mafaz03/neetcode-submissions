class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()

        min_heap = []
        heapq.heappush(min_heap, [0, points[0]])

        for i in points[1:]:
            heapq.heappush(min_heap, [abs(points[0][0] - i[0]) + abs(points[0][1] - i[1]), i])

        res = 0

        while len(visited) != len(points):
            c, point = heapq.heappop(min_heap)
            
            if tuple(point) in visited:
                continue

            # print(c, point)
            res += c
            visited.add(tuple(point))

            for p in points:
                heapq.heappush(min_heap, [abs(point[0] - p[0]) + abs(point[1] - p[1]), p])
            
        return res