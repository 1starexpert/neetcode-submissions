# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """
        curr = l1
        curr2 = l2
        size1 = 1
        size2 = 1
        carry = 0

        while curr.next is not None:
            size1 += 1
            curr = curr.next
        while curr2.next is not None:
            size2 += 1
            curr2 = curr2.next
        curr = l1
        curr2 = l2
        if size1 > size2:
            while curr is not None:
                if curr2 is None:
                    val = curr.val + 0 + carry
                    carry = val // 10
                    curr.val = val % 10
                    if curr.next is None:
                        if carry != 0:
                            new_node = ListNode(carry)
                            curr.next = new_node
                            break
                    curr = curr.next
                    continue
                val = curr.val + curr2.val + carry
                carry = val // 10
                curr.val = val % 10
                curr = curr.next
                curr2 = curr2.next
            return l1

        else:
            while curr2 is not None:
                if curr is None:
                    val = curr2.val + 0 + carry
                    carry = val // 10
                    curr2.val = val % 10
                    if curr2.next is None:
                        if carry != 0:
                            new_node = ListNode(carry)
                            curr2.next = new_node
                            break
                    curr2 = curr2.next
                    continue
                val = curr.val + curr2.val + carry
                carry = val // 10
                curr2.val = val % 10
                if curr.next is None and curr2.next is None:
                    if carry != 0:
                            new_node = ListNode(carry)
                            curr2.next = new_node
                    break
                curr = curr.next
                curr2 = curr2.next
 
            return l2
