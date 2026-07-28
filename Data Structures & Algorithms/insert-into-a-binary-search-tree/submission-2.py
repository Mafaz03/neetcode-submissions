# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)

        desired = root.left if val < root.val else root.right
        
        curr_prev = None
        while desired:
            curr_prev = desired
            desired = desired.left if val < desired.val else desired.right
        
        curr_dummy = root if not curr_prev else curr_prev
        
        if val < curr_dummy.val:
            curr_dummy.left = TreeNode(val)
        else:
            curr_dummy.right = TreeNode(val)
    

        return root
        