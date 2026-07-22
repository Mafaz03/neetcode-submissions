class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        PrefixSum = {} # {sum: no. of ways}
        PrefixSum[0] = 1

        summ = 0
        res  = 0

        for n in nums:
            summ += n

            to_remove = summ - k
            if to_remove in PrefixSum:
                res += PrefixSum[to_remove]
            
            if summ in PrefixSum: PrefixSum[summ] += 1
            else: PrefixSum[summ] = 1

        return res

