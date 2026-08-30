class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # res = x

        # for _ in range(n-1):
        #     res = (res + 1) | x
        # return res

        res = x
        i = 1
        j = 1

        while j <= (n-1):
            if (i & x == 0):
                if (j & n-1 != 0):
                    res = res | i
                j = j << 1
            i = i << 1
        return res