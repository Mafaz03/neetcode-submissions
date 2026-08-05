class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]):

        arr = sorted(zip(capital, profits))
        heap = []

        i = 0
        n = len(arr)

        for _ in range(k):

            while i < n and arr[i][0] <= w:
                heapq.heappush(heap, -arr[i][1])
                i += 1

            if not heap:
                break

            w += -heapq.heappop(heap)

        return w