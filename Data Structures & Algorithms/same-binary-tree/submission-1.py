# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([p])
        dq2 = deque([q])

        while dq and dq2:
            node = dq.popleft()
            node2 = dq2.popleft()

            

            if not node and not node2:
                continue
            
            if (node and not node2) or (not node and node2):
                return False


            if node.val != node2.val: 
                return False



            dq.append(node.left)
            dq.append(node.right)

            dq2.append(node2.left)
            dq2.append(node2.right)

            
        return True if len(dq) == 0 and len(dq2) == 0 else False