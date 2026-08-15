class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curr_sum_min = 0
        curr_sum_max = 0

        min_sum = float("inf")
        max_sum = float("-inf")

        for num in nums:
            curr_sum_min += num
            curr_sum_max += num

            min_sum = min(min_sum, curr_sum_min)
            max_sum = max(max_sum, curr_sum_max)

            if curr_sum_min > 0: curr_sum_min = 0
            if curr_sum_max < 0: curr_sum_max = 0
        
        if max_sum < 0:
            return max_sum
        
        return max(sum(nums) - min_sum, max_sum)