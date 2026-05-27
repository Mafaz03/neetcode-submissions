class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] in nums[i+1:]: 
                return True
        
        return False
