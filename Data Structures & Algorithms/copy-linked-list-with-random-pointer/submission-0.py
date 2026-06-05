"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # storing random values and idx
        hashmap = {} # {node: idx}

        dummy = head
        idx = 0
        while dummy:
            hashmap[dummy] = idx
            dummy = dummy.next
            idx += 1
            
        hashmap_rev = {v: k for k, v in hashmap.items()} # idx: old node


        hashmap_2 = {} # {node: random_idx}
        dummy = head
        idx = 0
        while dummy:
            if dummy.random == None:
                hashmap_2[dummy] = None
            else:
                hashmap_2[dummy] = hashmap[dummy.random]
            dummy = dummy.next
            idx += 1
        
        # making new nodes without random 
        n = len(hashmap)
        nodes_all = []
        for i in range(0, n, 1):
            nodes_all.append(Node(hashmap_rev[i].val, next = None, random = None))


        connection = {} # {old node: new node}
        for i in range(n):
            connection[hashmap_rev[i]] = nodes_all[i]


        head = Node(0)
        head_d = head
        for node_idx in range(n):
            head_d.next = nodes_all[node_idx]
            head_d = head_d.next

        connect_rand = head.next
        for i in range(n):

            if hashmap_2[hashmap_rev[i]] is None:
                connect_rand.random = None
            else:
                connect_rand.random = connection[hashmap_rev[hashmap_2[hashmap_rev[i]]]]
            connect_rand = connect_rand.next

                
        return head.next



            