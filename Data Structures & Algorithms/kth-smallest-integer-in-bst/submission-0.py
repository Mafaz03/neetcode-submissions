# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]

        def dfs(root):
            if root == None:
                return None
            
            
            left = dfs(root.left)
            if left is not None:
                return left


            count[0] += 1
            if count[0] == k:
                return root.val

            # print(root.val, end = " ")
            right = dfs(root.right)
            if right is not None:
                return right

        return dfs(root)