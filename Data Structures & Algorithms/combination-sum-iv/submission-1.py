class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {}

        def dfs(target):
            if target < 0:
                return 0

            if target == 0:
                return 1

            if target in mem:
                return mem[target]

            count = 0
            for num in nums:
                count += dfs(target - num)     
                
            mem[target] = count
            return count

        return dfs(target)  