# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        elements = []

        dq = deque([root])

        while dq:
            
            node = dq.popleft()

            if node is None:
                elements.append(None)
                continue

            elements.append(node.val)

            dq.append(node.left)
            dq.append(node.right)

        for i in range(len(elements)):
            if elements[len(elements) - i - 1] != None: break

        elements = elements[:len(elements) - i]
        return '*'.join([str(i) for i in elements])
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        deserialised_bfs = [int(i) if i != "None" else None for i in data.split("*")]
        
        if len(deserialised_bfs) == 1 and deserialised_bfs[0] is None: 
            return None

        i = 1
        root = TreeNode(deserialised_bfs[0])
        dq = deque([root])

        while dq and i < len(deserialised_bfs):
            node = dq.popleft()

            if i < len(deserialised_bfs) and deserialised_bfs[i] is not None:
                node.left = TreeNode(deserialised_bfs[i])
                dq.append(node.left)
            
            i += 1

            if i < len(deserialised_bfs) and deserialised_bfs[i] is not None:
                node.right = TreeNode(deserialised_bfs[i])
                dq.append(node.right)
            i += 1
        
        return root







