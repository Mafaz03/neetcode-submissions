class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        furthest = 0

        while idx < len(nums):
            if idx > furthest:
                return False

            furthest = max(furthest, idx + nums[idx])
            idx += 1
        return True