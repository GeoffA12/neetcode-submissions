# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Start at the head of the LL, continue until node == None
2. Maintain two pointers, 1 to the current node, and another to prev. prev will start off as null
3. At each iteration, if prev is set current node's next pointer to prev. 
4. Set prev to the current node, the move node to node.next
5. Return node
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = head
        prev = None

        while traverse != None:
            original_next = traverse.next
            traverse.next = prev
            prev = traverse
            traverse = original_next
        
        return prev
        