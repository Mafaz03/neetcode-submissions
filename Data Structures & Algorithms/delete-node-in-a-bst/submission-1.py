# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # goal delete the biggest out of the left sub tree

        if not root:
            return None

        # reach the node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else: 
            # key found
            if not root.left: # left is Null
                return root.right
            
            elif not root.right: # right is Null
                return root.left
            
            else: # 2 children
                curr = root.left

                while curr.right:
                    curr = curr.right

                # Copy predecessor value
                root.val = curr.val

                # Delete duplicate from left subtree
                root.left = self.deleteNode(root.left, curr.val)
        return root



        