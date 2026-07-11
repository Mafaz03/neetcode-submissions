# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
        
#         cache = {} # {summ: ways}


#         def dfs(summ, i):
#             if summ == amount:
#                 return 1
            
#             if summ > amount:
#                 return 0
            
#             if (summ,i) in cache:
#                 return cache[(summ,i)]
            
#             ans = 0

#             for idx, coin in enumerate(coins[i:]):
#                 summ += coin
#                 ans += dfs(summ, idx+i)
#                 summ -= coin
            
#             cache[(summ,i)] = ans

#             return ans

#         return dfs(0, 0)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev_row = [0] * (amount+1)
        prev_row[0] = 1

        next_row = [0] * (amount+1)
        next_row[0] = 1

        for i in reversed(range(len(coins))):

            for j in range(1,amount+1):
                
                to_make = j - coins[i]

                if to_make >= 0:
                    next_row[j] += next_row[to_make]

                if i != len(coins)-1:
                    next_row[j] += prev_row[j]
            
            # print(prev_row)

            prev_row = next_row

            next_row = [0] * (amount+1)
            next_row[0] = 1
        
        return prev_row[-1]