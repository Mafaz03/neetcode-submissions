# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def delete(parent, node):

            if not node:
                return 
            
            delete(node, node.left)
            delete(node, node.right)

            if (node.val == target) and (not node.left) and (not node.right):
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        
        delete(root, root)
        
        if (not root.left) and (not root.right) and (root.val == target):
            return 
    
        return root

        
        