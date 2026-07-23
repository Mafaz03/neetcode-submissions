class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def shipCap(cap):
            ships = 1
            currCap = cap

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        L = max(weights)
        R = sum(weights)
        res = R

        while L <= R:
            mid = (L+R)//2
            if shipCap(mid):
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1
        return res