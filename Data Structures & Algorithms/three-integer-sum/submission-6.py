class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sol = []

        n = len(nums)

        nums = sorted(nums)

        for idx, num in enumerate(nums):
            if idx == 0 or num != nums[idx-1]: 
                # two sum

                l = idx + 1
                r = n-1
                while l < r:
                    temp_sum = nums[l] + nums[r]
                
                    if temp_sum + num < 0:
                        l += 1
                    elif temp_sum + num > 0:
                        r -= 1
                    else:
                        sol.append([num, nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        return sol