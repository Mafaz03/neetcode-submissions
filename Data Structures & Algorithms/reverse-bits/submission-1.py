class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # 1 2 4 8
        
        power = 31
        while n:
            if (n & 1):
                res += 2**power
            n = n >> 1
            power -= 1
        return res