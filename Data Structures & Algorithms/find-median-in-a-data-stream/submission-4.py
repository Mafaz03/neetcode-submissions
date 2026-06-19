class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)
        

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == len(self.minheap) == 0: # initial
            heapq.heappush(self.maxheap, -num)
        
        else:
            if num < -self.maxheap[0]: # add to max heap
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0: # even if its even and its not divided equally
            if len(self.maxheap) > len(self.minheap):
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            elif len(self.maxheap) < len(self.minheap):
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))


    def findMedian(self) -> float:
        maxh = len(self.maxheap)
        minh = len(self.minheap)
        
        if maxh - minh == 1:
            return -self.maxheap[0]
        elif minh - maxh == 1:
            return self.minheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0])/2
             