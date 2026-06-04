# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_p = head
        fast_p = head.next

        # finding mid
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next



        temp_slow = slow_p.next
        slow_p.next = None

        # reverse connection for second half
        prev, curr = None, temp_slow

        while curr:
            temp_p = curr.next
            curr.next = prev
            prev = curr
            curr = temp_p



        forward = head
        reverse = prev

        while reverse:
            temp_f = forward.next
            temp_r = reverse.next
            
            forward.next = reverse
            reverse.next = temp_f

            reverse = temp_r
            forward = temp_f
