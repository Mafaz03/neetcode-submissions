class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] < 0: nums[idx] = 0
        
        for idx in range(len(nums)):
            value = abs(nums[idx])
            
            if 1 <= value <= len(nums):
                
                if nums[value - 1] > 0:
                    nums[value - 1] *= -1
                
                elif nums[value - 1] == 0:
                    nums[value - 1] = float("-inf")

        
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i

        return len(nums) + 1
            
                


                
