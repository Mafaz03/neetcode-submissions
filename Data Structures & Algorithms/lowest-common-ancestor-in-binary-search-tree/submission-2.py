# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dq = deque([root])
        # print(p.val)

        while dq:
            poped = dq.popleft()

            left = None
            if poped.left:
                left = poped.left
                dq.append(poped.left)
            
            right = None
            if poped.right:
                right = poped.right
                dq.append(poped.right)
            
            if (poped.val < p.val and poped.val > q.val) or (poped.val < q.val and poped.val > p.val): # split occurs
                return poped
            
            if poped.val == p.val or poped.val == q.val:
                return poped
            




