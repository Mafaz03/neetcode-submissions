# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height_of_bst(self, root):
        if not root:
            return 0
        
        left_height = self.height_of_bst(root.left)
        if left_height == -1:
            return -1

        right_height = self.height_of_bst(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        height = self.height_of_bst(root)

        return False if height == -1 else True
        