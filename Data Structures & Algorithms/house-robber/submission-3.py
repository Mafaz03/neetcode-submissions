class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        first  = nums[0]
        second = max(first, nums[1])

        for i in range(2, len(nums)):
            # choose not to rob vs choose to rob
            temp = max(second, nums[i] + first)
            print(temp)
            first = second
            second = temp
        return second