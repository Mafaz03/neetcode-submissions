# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack  = []

        curr = root

        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            curr = curr.right

        # def dfs(root):
        #     if not root:
        #         return 
            
        #     result.append(root.val)   
        #     dfs(root.left)
        #     dfs(root.right)
            
        # dfs(root)
        
        return result
        