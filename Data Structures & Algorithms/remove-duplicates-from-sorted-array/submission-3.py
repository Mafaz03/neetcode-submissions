class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1

        while i < len(nums):

            while (i < len(nums)) and ((nums[i] == nums[i-1]) or (nums[i] < nums[j-1])):
                i += 1

            if i < len(nums):
                nums[j] = nums[i]
                j += 1
                i += 1
                
        return j