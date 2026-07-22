class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            to_add = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = to_add
        