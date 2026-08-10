# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        brute force solution
        """
        arr = []

        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        l = 0
        r = len(arr) - 1

        head = arr[l]
        l += 1
        curr = head
        while l <= r:
            if l == r:
                curr.next = arr[r]
                curr = curr.next
                break
            curr.next = arr[r]
            curr = curr.next
            curr.next = arr[l]
            curr = curr.next
            l += 1
            r -= 1
        curr.next = None
        
        
