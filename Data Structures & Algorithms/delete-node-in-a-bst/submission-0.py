# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent_of_key = None

        while curr and curr.val != key:
            parent_of_key = curr
            curr = curr.left if key < curr.val else curr.right

        if curr == None:
            return root

        def replace(node):
            nonlocal root
            if parent_of_key == None:
                root = node
            elif parent_of_key.left == curr:
                parent_of_key.left = node
            else:
                parent_of_key.right = node
            
        # no children
        if (not curr.left) and (not curr.right):
            replace(None)
        
        # 1 children
        elif (curr.left) and (not curr.right):
            replace(curr.left)
        elif (not curr.left) and (curr.right):
            replace(curr.right)

        # 2 children
        else:
            max_parent = curr
            max_node = curr.left

            while max_node.right:
                max_parent = max_node
                max_node = max_node.right

            if max_parent != curr:
                max_parent.right = max_node.left
                max_node.left = curr.left
                
            max_node.right = curr.right

            replace(max_node)
    
        return root







        