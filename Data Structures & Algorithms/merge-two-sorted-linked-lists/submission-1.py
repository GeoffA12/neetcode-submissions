# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        head = None

        lp = list1
        rp = list2

        while lp != None or rp != None:
            if lp and rp:
                if lp.val <= rp.val:
                    if dummy:
                        dummy.next = lp
                        dummy = dummy.next
                    else:
                        dummy = lp
                        head = dummy
                    lp = lp.next
                else:
                    if dummy:
                        dummy.next = rp
                        dummy = dummy.next
                    else:
                        dummy = rp
                        head = dummy
                    rp = rp.next
            elif lp and not rp:
                if dummy:
                    dummy.next = lp
                    dummy = dummy.next
                else:
                    dummy = lp
                    head = dummy
                lp = lp.next
            
            elif rp and not lp:
                if dummy:
                    dummy.next = rp
                    dummy = dummy.next
                else:
                    dummy = rp
                    head = dummy
                rp = rp.next
        
        return head
        