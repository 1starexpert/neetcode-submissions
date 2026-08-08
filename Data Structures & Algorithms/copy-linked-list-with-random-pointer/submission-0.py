"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        n -> n -> n -> n -> NULL
        """
        orig_list = { None : None}

        curr = head
        while curr:
            copy_node = Node(curr.val)
            orig_list[curr] = copy_node
            curr = curr.next
        
        curr = head
        while curr:
            copy = orig_list[curr]
            copy.next = orig_list[curr.next]
            copy.random = orig_list[curr.random]
            curr = curr.next
        
        return orig_list[head]
        

        