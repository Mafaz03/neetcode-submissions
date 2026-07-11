class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp   = [1] * len(nums)

        for i in range(len(nums)):
            best = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, dp[j])

            dp[i] = best + 1
        
        return max(dp)