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

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.add_2_ll(l1, l2))

            lists = merged
        return lists[0]