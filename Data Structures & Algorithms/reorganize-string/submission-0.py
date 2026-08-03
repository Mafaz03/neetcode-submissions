class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)

        if max(counter.values()) > math.ceil(len(s)/2): return ""

        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, [-v,k])

        r = ""

        while heap:
            count, char = heapq.heappop(heap)
            count = -count
            
            print(char, count)

            if r and r[-1] == char:
                count2, char2 = heapq.heappop(heap)
                count2 = -count2

                heapq.heappush(heap, [-count, char])

                r += char2
                if count2 != 1:
                    count2 -= 1
                    heapq.heappush(heap, [-count2, char2])

            else:
                r += char
                if count != 1:
                    count -= 1
                    heapq.heappush(heap, [-count, char])
        return r