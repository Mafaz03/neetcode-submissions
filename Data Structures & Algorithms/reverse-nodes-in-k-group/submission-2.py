# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rev_p = check_p = head

        num = 0
        ll_list = []

        while check_p:
            num += 1
            print(check_p.val, num)
            if num == k: 
                num = 0

                # reverse ll's nodes k times
                times = 0
                prev = None
                while rev_p and times < k:
                    temp = rev_p.next
                    rev_p.next = prev
                    prev = rev_p
                    rev_p = temp

                    times += 1

                ll_list.append(prev)
                check_p = rev_p
                

            else: check_p = check_p.next    

        if rev_p:
            ll_list.append(rev_p)

        while len(ll_list) != 1:
            curr = ll_list[-2]
            
            while curr.next:
                curr = curr.next
            
            curr.next = ll_list[-1]
            ll_list.pop()

        return ll_list[0]