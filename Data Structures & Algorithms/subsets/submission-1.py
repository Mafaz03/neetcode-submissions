class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # subset = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])    # TAKE
            dfs(i + 1, subset)

            subset.pop()              # UNDO TAKE
            dfs(i + 1, subset)        # SKIP
        
        dfs(0, [])
        return res