# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add_2_ll(self, ll1, ll2):
        curr = ListNode(0)
        d = curr

        while ll1 and ll2:
            if ll1.val < ll2.val:
                d.next = ListNode(ll1.val)
                ll1 = ll1.next
            else:
                d.next = ListNode(ll2.val)
                ll2 = ll2.next
            d = d.next

        if ll1:
            d.next = ll1
        if ll2:
            d.next = ll2
        
        return curr.next  


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        while len(lists) != 1:
            sorted_ll = self.add_2_ll(lists[0], lists[1])
            lists = lists[1:]
            lists[0] = sorted_ll
        return lists[0]