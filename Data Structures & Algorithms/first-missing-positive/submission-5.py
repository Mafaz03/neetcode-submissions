class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        minn = min(nums)
        # minn = 0 if minn < 0 else minn
        maxx = max(nums)

        for n in range(1,maxx+2):
            if n > 0 and n not in nums:
                return n

        return 1