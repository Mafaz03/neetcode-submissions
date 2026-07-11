class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 > len(edges): return False

        hashmap = {i:set() for i in range(n)}

        for u, v in edges:
            hashmap[u].add(v)
            hashmap[v].add(u)

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for nei in hashmap[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return False
                
                if not dfs(nei, node):
                    return False

            return True

        b = dfs(0, -1)

        if b:
            if len(visited) != n: 
                print("because")
                return False

        return b

