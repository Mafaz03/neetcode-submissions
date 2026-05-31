class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        
        idx = -1

        while L <= R:
            # print(nums[L: R+1])

            mid = (L + R)//2

            # print(mid)

            if nums[mid] == target:
                idx = mid

            if nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return idx