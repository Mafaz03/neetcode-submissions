class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hash = {} # {(index: buy/sell): profit}

        profit = [0]

        def dfs(index, buy: bool):

            if index == len(prices):
                return 0

            if (index, buy) in hash:
                return hash[(index, buy)]

            if buy: # can sell today or skip
                profit[0] = max(dfs(index + 1, buy = False) - prices[index],  # buy today
                                dfs(index + 1, buy = True))                   # buy next day
            else:
                profit[0] = max(dfs(index + 1, buy = True) + prices[index], # sell today
                                dfs(index + 1, buy = False))                # sell next day
                            
            hash[(index, buy)] = profit[0]
            return profit[0]   


        return dfs(0, buy = True)