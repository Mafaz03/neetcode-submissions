class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-i for i in list(Counter(tasks).values())]
        heapq.heapify(max_heap)

        dq = deque([])

        T = 0

        while max_heap or dq:
            occurance = 0
            
            if max_heap:
                occurance = heapq.heappop(max_heap)
                occurance += 1 # reducing number of occurance

            T += 1
            
            if occurance != 0: 
                dq.append((occurance, n+T))

            if dq and dq[0][1] == T: # time out ended for that character and can be added back to max heap
                heapq.heappush(max_heap, dq.popleft()[0])

        return T