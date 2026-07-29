"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def makeTree(n, r, c):
            flag = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        flag = False
                        break
            if flag:
                return Node(grid[r][c], True)
            else:
                n = n // 2
                topLeft     = makeTree(n, r, c)
                topRight    = makeTree(n, r, c + n)
                bottomLeft  = makeTree(n, r + n, c)
                bottomRight = makeTree(n, r + n, c + n)

                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
            
        n = len(grid)
        return makeTree(n, 0, 0)
        