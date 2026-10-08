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

        def is_same(grid):
            first = grid[0][0]

            for row in grid:
                for x in row:
                    if x != first:
                        return False

            return True

        def makeTree(nested_list):

            # 1. All values are same
            if is_same(nested_list):
                return Node(
                    nested_list[0][0],
                    1,
                    None, None, None, None
                )

            # 2. Split into 4 parts
            n = len(nested_list)
            mid = n // 2

            top_left = []
            top_right = []
            bottom_left = []
            bottom_right = []

            for i in range(mid):
                top_left.append(nested_list[i][:mid])
                top_right.append(nested_list[i][mid:])

            for i in range(mid, n):
                bottom_left.append(nested_list[i][:mid])
                bottom_right.append(nested_list[i][mid:])

            # 3. Recursively construct the 4 children
            topLeft = makeTree(top_left)
            topRight = makeTree(top_right)
            bottomLeft = makeTree(bottom_left)
            bottomRight = makeTree(bottom_right)

            # 4. Current node is not a leaf
            return Node(
                0,                  # val can be 0
                0,                  # isLeaf = False
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return makeTree(grid)