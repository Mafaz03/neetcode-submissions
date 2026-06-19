class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) != 1:

            
            if not heap: break
            x = heapq.heappop(heap)
            if not heap: break
            y = heapq.heappop(heap)

            res = abs(x - y)
            if res > 0:
                heapq.heappush(heap, -res)

        return -heap[0] if len(heap) > 0 else 0