class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {} # {summ: ways}


        def dfs(summ, i):
            if summ == amount:
                return 1
            
            if summ > amount:
                return 0
            
            if (summ,i) in cache:
                return cache[(summ,i)]
            
            ans = 0

            for idx, coin in enumerate(coins[i:]):
                summ += coin
                ans += dfs(summ, idx+i)
                summ -= coin
            
            cache[(summ,i)] = ans

            return ans

        return dfs(0, 0)