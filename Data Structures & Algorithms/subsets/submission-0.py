class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])    # TAKE
            dfs(i + 1)

            subset.pop()              # UNDO TAKE
            dfs(i + 1)        # SKIP
        
        dfs(0)
        return res