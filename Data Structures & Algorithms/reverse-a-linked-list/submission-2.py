# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_prev, p_recent   = None, head

        while p_recent:
            temp_p = p_recent.next
            p_recent.next = p_prev
            p_prev = p_recent
            p_recent = temp_p

        return p_prev