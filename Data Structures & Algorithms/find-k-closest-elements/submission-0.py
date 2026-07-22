class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(i-x) for i in arr]
        minn = min(diff)

        l = 0
        r = 0

        for idx, d in enumerate(diff):
            if d == minn:
                l = r = idx
                break

        while k-1:
            if l-1 >= 0 and r+1 < len(arr):
                if diff[l-1] < diff[r+1]:
                    l -= 1
                elif diff[l-1] > diff[r+1]:
                    r += 1
                else:
                    l -= 1

            elif l-1 < 0:
                r += 1

            else:
                l -= 1

            k -= 1

        return arr[l:r+1]