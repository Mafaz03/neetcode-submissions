class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

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

        return dfs(0, -1) and len(visited) == n

        # if b:
        #     if : 
        #         print("because")
        #         return False

        # return b

