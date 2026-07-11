class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        nums += list(range(0,len(nums)+1))

        for n in nums:
            res = res ^ n
        
        return res