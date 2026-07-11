class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:set() for i in range(n)}

        for u, v in edges:
            hashmap[u].add(v)
            hashmap[v].add(u)


        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in hashmap[node]:
                if nei == parent: 
                    continue # this is because child and parent node are undirected

                if nei not in visited:
                    dfs(nei, node)

            return True


        # dfs(0, -1)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count