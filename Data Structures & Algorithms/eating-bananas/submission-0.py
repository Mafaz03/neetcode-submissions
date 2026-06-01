class Solution:

    def check(self, piles, bph):
        t = 0
        for p in piles:
            t += math.ceil(p/bph)
        return t
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles)

        minimum_time_required = max_val

        L, R = min_val, max_val

        while L <= R:
            mid = (L+R)//2
            print(L, mid, R)

            time_taken = self.check(piles, mid)

            if time_taken <= h:
                minimum_time_required = min(minimum_time_required, mid)
                R = mid - 1
            else:
                L = mid + 1
        return minimum_time_required