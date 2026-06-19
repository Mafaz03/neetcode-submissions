class Solution:
    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash = {}
        for x,y in points:
            dis = self.distance(x,y)
            if dis in hash:
                hash[dis].append([x,y])
            else:
                hash[dis] = [[x,y]]


        heap = list(hash.keys())
        heapq.heapify(heap)


        smallest = heapq.nsmallest(k, heap)

        res = []
        for s in smallest:
            res.extend(hash[s])

        return res[:k]