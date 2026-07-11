class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for s, d in tickets:
            adj_list[s].append(d)

        for i in adj_list:
            adj_list[i] = sorted(adj_list[i])

        res = ["JFK"]

        def dfs(node):

            if len(res) == len(tickets) + 1:
                return True
            
            if node not in adj_list:
                return False
            
            # temp = list(adj_list[node])
            for idx, nei in enumerate(adj_list[node]):
                # print(node, idx, nei)

                adj_list[node].pop(idx)
                res.append(nei)

                if dfs(nei): 
                    return True
                
                adj_list[node].insert(idx, nei)
                res.pop()

            return False

        dfs("JFK")
        return res