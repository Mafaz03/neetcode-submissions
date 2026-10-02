class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_pos = 0

        for i, n in enumerate(nums):
            if farthest_pos < i: 
                break
            farthest_pos = max(farthest_pos, i + n)
            

        return farthest_pos >= len(nums)-1
