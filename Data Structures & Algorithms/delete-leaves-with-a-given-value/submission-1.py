# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 
            
            node.left =  dfs(node.left)
            node.right = dfs(node.right)

            if ((node.val == target) and (not node.left) and (not node.right)):
                return None

            return node

        node = dfs(root)

        def p_dfs(node):
            if not node: return 

            print(node.val)
            p_dfs(node.left)
            p_dfs(node.right)

        p_dfs(node)

        return node

        
        
        