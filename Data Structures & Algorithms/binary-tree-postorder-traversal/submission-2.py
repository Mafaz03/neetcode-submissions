# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack  = []
        curr   = root

        stack = [[root, False]]

        while stack:
            curr, visited = stack.pop()

            if not curr: 
                continue
            
            if visited:
                result.append(curr.val)

            else:
                stack.append([curr, True])
                if curr.right: stack.append([curr.right, False])
                if curr.left: stack.append([curr.left, False])

        return result

        