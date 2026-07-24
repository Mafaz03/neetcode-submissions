class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'mountainArr') -> int:
        n = mountainArr.length()
        # find peak index
        L = 1
        R = n - 2
        peak_idx = None

        while L <= R:
            mid = (L+R)//2

            mid_minus_1 = mountainArr.get(mid-1)
            mid_ = mountainArr.get(mid)
            mid_plus_1 = mountainArr.get(mid+1)

            if mid_minus_1 < mid_ > mid_plus_1:
                peak_idx = mid
                if mid_ == target: return mid
                break
            
            elif mid_minus_1 < mid_ < mid_plus_1:
                L = mid + 1
            
            elif mid_minus_1 > mid_ > mid_plus_1:
                R = mid - 1

        print(peak_idx)
        # search left
        found = -1

        L = 0
        R = peak_idx

        while L <= R:
            mid = (L+R)//2

            mid_ = mountainArr.get(mid)

            if mid_ == target:
                return mid
            
            elif mid_ < target:
                L = mid + 1
            
            else:
                R = mid - 1
        
        # search right

        L = peak_idx + 1
        R = n - 1

        while L <= R:
            mid = (L+R)//2

            mid_ = mountainArr.get(mid)

            if mid_ == target:
                return mid
            
            elif mid_ < target:
                R = mid - 1
            
            else:
                L = mid + 1
            

        return -1






