class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap = []
        
        arr = []
        for i in range(len(profits)):
            arr.append([capital[i], profits[i]])
        
        arr = sorted(arr, key = lambda x: x[0])

        while arr and arr[0][0] <= w:
            heapq.heappush(heap, -arr[0][1])
            arr = arr[1:]

        # print("arr: ", arr)
        # print("heap: ", heap)

        
        if heap:
            while (k != 0):
                w += (-heapq.heappop(heap))
                # print(arr, heap, w)

                k -= 1
                
                while arr and arr[0][0] <= w:
                    # print(arr)
                    heapq.heappush(heap, -arr[0][1])
                    arr = arr[1:]
                
        return w


        




