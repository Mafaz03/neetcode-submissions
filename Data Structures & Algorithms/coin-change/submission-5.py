class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(summ):
            
            if summ == amount:
                return 0 # add nothing
            
            if summ > amount:
                return float("inf") # not possible
            
            if summ in mem:
                # print("hit, ", summ)
                return mem[summ]
            
            ans = float("inf") # local shortest path
            for coin in coins:
                ans = min(ans, 1+dfs(summ+coin))

            mem[summ] = ans

            return ans

        res = dfs(0)
        return res if res < float("inf") else -1