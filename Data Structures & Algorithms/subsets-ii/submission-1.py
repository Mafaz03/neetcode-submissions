class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)


        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop()
            next_i = i+1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1

            backtrack(next_i, subset)


        backtrack(0, [])
        return res