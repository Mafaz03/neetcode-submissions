class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        for i, n_0 in enumerate(nums):

                for idx in range(i+1, len(nums)):
                        
                        num = nums[idx]

                        l = idx + 1
                        r = len(nums) - 1

                        while l < r:
                            if (n_0 + num + nums[l] + nums[r]) - target < 0:
                                l += 1 # make number bigger
                            elif (n_0 + num + nums[l] + nums[r]) - target > 0:
                                r -= 1 # make the number smaller
                            else: 
                                result.add((n_0, num, nums[l], nums[r]))

                                l += 1
                                r -= 1
                            
        return list(result)