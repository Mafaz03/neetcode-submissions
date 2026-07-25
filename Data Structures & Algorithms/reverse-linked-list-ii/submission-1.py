# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left: return head
        
        left_prev = None
        left_ll = head
        

        for _ in range(left - 1):
            left_prev = left_ll
            left_ll = left_ll.next

        if left_prev:
            left_prev.next = None # break the chain
        # print(left_ll.val)
        # print(left_prev.val)

        right_ll = left_ll
        for _ in range(right-left):
            right_ll = right_ll.next
            
        right_next = right_ll.next
        right_ll.next = None

        # print(right_ll.val)
        # print(right_next.val)

        temp_head = left_ll

        prev = right_next
        while left_ll:
            temp = left_ll.next
            left_ll.next = prev
            prev = left_ll
            left_ll = temp

        if left_prev:
            left_prev.next = prev
            return head
        else:
            return prev
    
        


