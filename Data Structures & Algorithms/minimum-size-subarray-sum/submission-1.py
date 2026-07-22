class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        curr_sum = 0
        res = float("inf")

        for r in range(len(nums)):

            if nums[r] >= target:
                return 1

            curr_sum += nums[r]

            while curr_sum >= target:
                res = min(res, r-l+1)
                curr_sum -= nums[l]
                l += 1

        return res if res != float("inf") else 0