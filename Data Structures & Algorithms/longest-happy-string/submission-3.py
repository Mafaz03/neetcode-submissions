class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        # max heap
        heap = []

        if a > 0: heapq.heappush(heap, [-a, "a"])
        if b > 0: heapq.heappush(heap, [-b, "b"])
        if c > 0: heapq.heappush(heap, [-c, "c"])

        s = ""

        while heap:
            print(heap)
            if (not s) or (len(s) == 1) or ((len(s) >= 2) and (s[-1] != s[-2])):
                count, char = heapq.heappop(heap)
                count = -count

                count -= 1
                
                s += char

                if count > 0: heapq.heappush(heap, [-count, char])
            
            elif ((len(s) >= 2) and (s[-1] == s[-2])):
            # else:
                if len(heap) >= 2:
                    print("yess")
                    count1, char1 = heapq.heappop(heap)
                    count2, char2 = heapq.heappop(heap)
                    count1 = -count1
                    count2 = -count2

                    if char2 != s[-1]:
                        s += char2
                        count2 -= 1
                    else:
                        s += char1
                        count1 -= 1


                    if count1 > 0: heapq.heappush(heap, [-count1, char1])
                    if count2 > 0: heapq.heappush(heap, [-count2, char2])
                
                else:
                    print("nooo")
                    break

            print(heap)
            print("--")
        return s







