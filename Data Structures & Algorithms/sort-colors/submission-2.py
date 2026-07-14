class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        l = 0
        r = len(nums)-1
        i = 0

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1

            elif nums[i] == 2:
                swap(r, i)
                r -= 1
            
            else:
                i += 1
            

        