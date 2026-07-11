class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xffffffff 
        max  = 0x7fffffff 

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max else ~(a ^ mask)