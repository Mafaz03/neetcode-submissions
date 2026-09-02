# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            num1 = curr.val
            num2 = curr.next.val
            
            num_gcd = self.gcd(num1, num2)
            node_gcd = ListNode(num_gcd)

            node_gcd.next = curr.next
            curr.next = node_gcd

            curr = curr.next.next
        
        return head


    
        