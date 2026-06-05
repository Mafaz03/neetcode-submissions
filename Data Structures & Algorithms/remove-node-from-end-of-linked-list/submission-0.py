# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of ll
        len_1 = 0
        dummy_len = head
        while dummy_len:
            len_1 += 1
            dummy_len = dummy_len.next
        
        if len_1 == 1: return None
        if len_1 - n == 0: return head.next

        # deletting len_1 - n node
        first = None
        second = head
        temp_len_l = 0
        while temp_len_l <= len_1 - n:
            if temp_len_l == len_1 - n:
                print("wow")
                first.next = second.next
                # second = second.next

            else:
                first = second
                second = second.next
                

            temp_len_l += 1

        return head