# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def postorder(root):
            if not root:
                return [0, 0]

            left_pair  = postorder(root.left)
            right_pair = postorder(root.right)

            return [root.val + left_pair[1] + right_pair[1], max(left_pair) + max(right_pair)]
            

        return max(postorder(root))