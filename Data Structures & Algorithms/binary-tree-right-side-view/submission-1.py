# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        master = []

        dq = deque([root])
        while dq:
            inner = []
            
            for _ in range(len(dq)):
                poped = dq.popleft()
                inner.append(poped.val)

                if poped.left:
                    dq.append(poped.left)
                    
                if poped.right:
                    dq.append(poped.right)
                
            master.append(inner[-1])

        return master