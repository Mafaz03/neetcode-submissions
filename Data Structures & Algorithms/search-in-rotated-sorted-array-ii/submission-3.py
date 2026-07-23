class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L+R)//2

            if (nums[mid] == target) or (nums[L] == target) or (nums[R] == target):
                return True

            while (L < R) and (nums[L] == nums[mid]):
                if nums[L] == target:
                    return True
                L += 1
            
            while (L < R) and (nums[R] == nums[mid]):
                if nums[R] == target:
                    return True
                R -= 1

            if (nums[mid] == target) or (nums[L] == target) or (nums[R] == target):
                return True

            mid = (L+R)//2

            if nums[mid] >= nums[L]:              # we are in left portion
                if nums[L] <= target < nums[mid]: # target is in left portion
                    R = mid - 1
                else:
                    L = mid + 1

            else:                                 # we are in right portion
                if nums[mid] < target <= nums[R]: # target is in right portion
                    L = mid + 1
                else:
                    R = mid - 1
        
        return False

                