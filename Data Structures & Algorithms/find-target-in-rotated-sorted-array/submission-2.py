class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found_idx = -1
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L+R)//2
            print(L, mid, R)

            if nums[mid] == target: # rotation found
                # print("found: ", mid)
                return mid

            if nums[mid] >= nums[0]:  # now i am in left sorted arr
                if target >= nums[0]: # target belongs to left sorted arr
                    if target < nums[mid]:
                        R = mid - 1
                    else:                # target is in right of mid
                        L = mid + 1
                else:
                    L = mid + 1
            else:                    # now i am in right sorted arr
                if target < nums[0]: # target belongs to right sorted arr
                    if target < nums[mid]:
                        R = mid - 1
                    else:                # target is in left of mif
                        L = mid + 1
                
                else:
                    R = mid - 1


        return -1