# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = right = dummy

        idx = 0
        while idx != n:
            right = right.next
            idx += 1

        left_left = head
        while right:
            left_left = left
            left = left.next
            right = right.next

        left_left.next = left.next

        return dummy.next