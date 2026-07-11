class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj_hash = {f: set() for f in range(n)}

        # for f in flights:
        #     adj_hash[f[0]].add((f[1], f[2]))


        # visited = set() 

        # res = [float("inf")]

        # def dfs(node, cost, depth):
        #     if depth > k + 1: 
        #         return
                
        #     if node == dst:
        #         res[0] = min(res[0], cost)
        #         return 
            
        #     if node in visited:
        #         return
            
        #     visited.add(node)

        #     # print(cost)

        #     for nei, c in adj_hash[node]:
        #         dfs(nei, cost + c, depth+1)

        #     visited.remove(node)  


        # dfs(src, 0, 0)
        # return res[0] if res[0] < float("inf") else -1

        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):
            temp_prices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                temp_prices[d] = min(temp_prices[d], prices[s] + p)
            prices = temp_prices
        return prices[dst] if prices[dst] != float("inf") else -1








