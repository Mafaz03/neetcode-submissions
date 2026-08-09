# class Solution:
#     def __init__(self):
#         self.visited = set()
#         self.min_height = float("inf")
#         self.nodes_more_than_min = set()

#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n == 1:
#             return [0]

#         self.adj = defaultdict(list) # {node: [connected nodes]}

#         for a, b in edges:
#             self.adj[a].append(b)
#             self.adj[b].append(a)

#         leaves = []
#         for leave, nodes in self.adj.items():
#             if len(nodes) == 1:
#                 leaves.append(leave)


#         heights = defaultdict(list)

#         for node in self.adj:
#             self.visited.clear()
#             self.visited.update(leaves)

#             height = self.bfs(node)

#             if height != -1:

#                 heights[height].append(node)

#                 if height > self.min_height:
#                     self.nodes_more_than_min.add(node)
#                 else:
#                     self.min_height = height
                
#         return heights[self.min_height]
            

#     def bfs(self, node):
#         height = -1

#         self.visited.add(node)
#         dq = deque([node])
        
#         while dq:
#             q = len(dq)

#             for _ in range(q):
#                 node = dq.popleft()

#                 if node in self.nodes_more_than_min:
#                     return -1
                
#                 for nxt in self.adj[node]:
#                     if nxt not in self.visited:
#                         self.visited.add(nxt)
#                         dq.append(nxt)

#             height += 1
#             if height > self.min_height: return -1

#         return height

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (n == 1):
            return [0]

        if (n == 2):
            return edges[0]

        adj = defaultdict(list) # {node: [connected nodes]}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        dq = deque()
        edge_count = {}

        for node, nei in adj.items():
            if len(nei) == 1:
                dq.append(node)
            
            edge_count[node] = len(nei)
        
        print(dq)
        print(edge_count)

    
        while dq:

            if n <= 2:
                return list(dq)

            for _ in range(len(dq)):
                node = dq.popleft()
                n -= 1

                for adj_node in adj[node]:
                    edge_count[adj_node] -= 1 # removing adj nodes
                    if edge_count[adj_node] == 1:
                        dq.append(adj_node)






        


