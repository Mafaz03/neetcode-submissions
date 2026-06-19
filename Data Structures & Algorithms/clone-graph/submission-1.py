"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        oldToNew = {} # {old node: new node}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] # return copy
            
            copy = Node(val = node.val, neighbors = None)
            oldToNew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(
                                      dfs(n) # returns a copy of its neighbors
                                    )
            return copy
        return dfs(node)