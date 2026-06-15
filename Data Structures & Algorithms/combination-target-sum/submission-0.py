class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, current, total):
            if i >= len(nums):
                return
            
            if total == target:
                res.append(current.copy())
                # print(current.copy())
                return
            
            if total > target:
                return 
            
            total += nums[i]
            current.append(nums[i])
            dfs(i, current, total)     # TAKE same

            current.pop()              # UNDO TAKE
            total -= nums[i]

            dfs(i + 1, current, total) # SKIP and take something else

        dfs(0, [], 0)
        return res
