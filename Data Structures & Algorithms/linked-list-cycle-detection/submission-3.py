# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        fast and slow method:
        """
        slow = head
        fast = head
        curr = head

        while fast is not None:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False

            if slow == fast:
                return True
        
        return False
