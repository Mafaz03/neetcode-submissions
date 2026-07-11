class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        def houserobber1(nums):
            first  = nums[0]
            second = max(first, nums[1])

            for i in range(2, len(nums)):
                temp = max(nums[i]+first, second)
                first = second
                second = temp
            return second
        
        return max(houserobber1(nums[:-1]), houserobber1(nums[1:]))
