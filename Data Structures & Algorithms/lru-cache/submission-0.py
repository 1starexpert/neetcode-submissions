class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # left = LRU, right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Remove node from the linked list
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert node immediately before right (MRU position)
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Move node to MRU position
            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create and insert new node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict LRU if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]

