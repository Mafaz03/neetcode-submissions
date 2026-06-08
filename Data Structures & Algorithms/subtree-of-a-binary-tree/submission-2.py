# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSame(self, root1, root2):
        dq1 = deque([root1])
        dq2 = deque([root2])

        while dq1 and dq2:
            node1 = dq1.popleft()
            node2 = dq2.popleft()

            if node1 == None and node2 == None:
                continue

            if (node1 == None and node2 != None) or (node1 != None and node2 == None):
                return False

            if node1.val != node2.val:
                return False

            # if len(dq2) == 0: return True

            dq1.append(node1.left)
            dq1.append(node1.right)

            dq2.append(node2.left)
            dq2.append(node2.right)

            
        if len(dq2) == 0: return True
        else: False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        dq_master = deque([root])

        while dq_master:
            node_master = dq_master.popleft()

            if node_master.val == subRoot.val:
                if self.isSame(node_master, subRoot):
                    return True
            
            if node_master.left:
                dq_master.append(node_master.left)

            if node_master.right:
                dq_master.append(node_master.right)
    
        return False
        









        