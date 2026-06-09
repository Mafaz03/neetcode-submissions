# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        if not root: return []

        # maximum nodes in each level = 2^n, n = 0,1,2.....
        master_list = []
        
        while dq:
            inner = []

            for _ in range(len(dq)):
                poped = dq.popleft()
                inner.append(poped.val)

                if poped.left:
                    dq.append(poped.left)
                if poped.right:
                    dq.append(poped.right)
            
            master_list.append(inner)
        return master_list





