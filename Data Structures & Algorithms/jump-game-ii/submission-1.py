class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        jumps = 0

        while r < len(nums)-1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i + nums[i])
            l, r = r + 1, furthest

            # print(nums[l:r+1])

            jumps += 1
        return jumps