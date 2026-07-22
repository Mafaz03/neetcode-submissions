class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(i-x) for i in arr]

        minn = diff[0]
        l = r = 0
        for i in range(1,len(diff)):
            if diff[i] < minn:
                minn = diff[i]
                l = r = i
            if diff[i] > minn: break

        while k-1:
            if l-1 >= 0 and r+1 < len(arr):
                if diff[l-1] > diff[r+1]:
                    r += 1
                else:
                    l -= 1

            elif l-1 < 0:
                r += 1

            else:
                l -= 1

            k -= 1

        return arr[l:r+1]