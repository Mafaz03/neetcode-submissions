class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]: return nums[0]

        L, R = 0, len(nums)-1

        min_val = float("inf")

        while L <= R:
            mid = (L+R)//2
            # print(L, mid, R)

            if nums[mid-1] > nums[mid]: # rotation found
                min_val = min(min_val, nums[mid])

            if nums[mid] >= nums[0]:
                L = mid + 1
            else:
                R = mid - 1
        return min_val