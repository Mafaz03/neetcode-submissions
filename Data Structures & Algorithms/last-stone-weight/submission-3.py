class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) != 1:

            
            if not heap: break
            x,y = heapq.heappop(heap), heapq.heappop(heap)

            res = abs(x - y)
            if res > 0:
                heapq.heappush(heap, -res)

        return -heap[0] if heap else 0