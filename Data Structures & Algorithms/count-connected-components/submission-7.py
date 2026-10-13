class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        not_visited = set()
        for a, b in edges:
            not_visited.add(a)
            not_visited.add(b)
        
        adj_hash = defaultdict(list)
        for a, b in edges:
            adj_hash[a].append(b)
            adj_hash[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited: 
                return
            visited.add(node)
            not_visited.remove(node)
            for nei in adj_hash[node]:
                dfs(nei)
        count = 0
        while not_visited:
            start_node = list(not_visited)[0]
            dfs(start_node)
            count += 1
            print(visited)
        return count + (n - len(visited))
    
        



        