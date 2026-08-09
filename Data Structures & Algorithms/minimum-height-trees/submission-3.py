class Solution:
    def __init__(self):
        self.visited = set()
        self.min_height = float("inf")
        self.nodes_more_than_min = set()

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        self.adj = defaultdict(list) # {node: [connected nodes]}

        for a, b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)

        heights = defaultdict(list)

        for node in self.adj:
            self.visited.clear()

            height = self.bfs(node)

            if height != -1:

                heights[height].append(node)

                if height > self.min_height:
                    self.nodes_more_than_min.add(node)
                else:
                    self.min_height = height
                    
                # self.min_height = min(self.min_height, height)
                
        
        return heights[min(heights.keys())]
            

    def bfs(self, node):
        height = -1

        self.visited.add(node)
        dq = deque([node])
        
        while dq:
            q = len(dq)

            for _ in range(q):
                node = dq.popleft()

                if node in self.nodes_more_than_min:
                    return -1
                
                for nxt in self.adj[node]:
                    if nxt not in self.visited:
                        self.visited.add(nxt)
                        dq.append(nxt)

            height += 1
            if height > self.min_height: return -1

        return height





        