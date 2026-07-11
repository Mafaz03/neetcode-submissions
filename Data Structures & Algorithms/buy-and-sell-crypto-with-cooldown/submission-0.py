class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # {(i, buying:bool): max_val}

        def dfs(i, buying):
            
            if i >= len(prices):
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            if buying: # after buying -> sell or cooldown
                ans = max(
                    dfs(i+1, 0) - prices[i], # buy today
                    dfs(i+1, 1)              # skip buying today
                )

            else: # after selling -> buy next day or cooldown
                ans = max(
                    dfs(i+2, 1) + prices[i], # sell today
                    dfs(i+1, 0)              # cooldown, sell next day
                )

            cache[(i, buying)] = ans
            
            return ans

        return dfs(0,1)