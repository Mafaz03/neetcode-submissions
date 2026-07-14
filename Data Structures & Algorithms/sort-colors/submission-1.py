class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = Counter(nums)
        for idx, n in enumerate(nums):
            if counter[0] > 0:
                to_replace = 0
            elif counter[1] > 0:
                to_replace = 1
            else:
                to_replace = 2

            nums[idx] = to_replace
            counter[to_replace] -= 1

        