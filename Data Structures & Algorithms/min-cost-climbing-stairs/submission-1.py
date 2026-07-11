class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def dfs(step_idx):
    
        #     if step_idx >= len(cost):
        #         return 0
            
        #     # print(step_idx)
        #     mimimum_val = cost[step_idx] + min(dfs(step_idx + 1), dfs(step_idx + 2))
            
        #     return mimimum_val

        # return min(dfs(0), dfs(1))

        first  = cost[0]
        second = cost[1]

        for i in range(2, len(cost)+1):
            if i == len(cost):
                return min(first, second)
            
            temp = second
            second = cost[i] + min(first, second)
            first = temp