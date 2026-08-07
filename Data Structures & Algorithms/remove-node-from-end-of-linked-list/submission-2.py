# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [1,2,3,4,5,6]   n = 3
        """
        # determine size
        curr = head
        size = 1
        
        while curr.next is not None:
            size += 1
            curr = curr.next
        
        index = size - n
        if size == 1:
            return None
        if index == 0:
            return head.next

        curr = head
        i = 0
        while i < index - 1:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
    
        return head
