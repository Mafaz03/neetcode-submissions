class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adj_hash = defaultdict(list)

        for a, b in edges:
            adj_hash[a].append(b)
            adj_hash[b].append(a)
        
        start = 0
        q = deque([start])
        
        visited = {start}

        while q:
            node = q.popleft()

            for nei in adj_hash[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited) == n