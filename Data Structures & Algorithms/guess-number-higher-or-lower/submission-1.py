# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n

        if n == 1: return 1

        while L <= R:
            mid = (L+R)//2
            
            r = guess(mid)

            if r == 0:
                return mid
            elif r == 1:
                L = mid + 1
            else:
                R = mid - 1

        
        