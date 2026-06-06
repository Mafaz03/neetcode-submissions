class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.hasmap = {}  # {key: Node}

        self.head = Node(0, 0)  # dummy
        self.left_p = None      # LRU node
        self.right_p = self.head  # MRU node

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hasmap:
            return -1

        node = self.hasmap[key]

        # already most recently used
        if node == self.right_p:
            return node.val

        # detach
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node == self.left_p:
            self.left_p = node.next

        # move to end
        self.right_p.next = node
        node.prev = self.right_p
        node.next = None
        self.right_p = node

        return node.val

    def put(self, key: int, value: int) -> None:

        # update existing key
        if key in self.hasmap:
            node = self.hasmap[key]
            node.val = value

            if node != self.right_p:

                # detach
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev

                if node == self.left_p:
                    self.left_p = node.next

                # move to end
                self.right_p.next = node
                node.prev = self.right_p
                node.next = None
                self.right_p = node

            return

        # evict LRU
        if len(self.hasmap) == self.capacity:

            lru = self.left_p

            self.hasmap.pop(lru.key)

            self.left_p = lru.next

            if self.left_p:
                self.left_p.prev = self.head
                self.head.next = self.left_p
            else:
                self.head.next = None
                self.right_p = self.head

        # insert new node
        node = Node(key, value)
        self.hasmap[key] = node

        self.right_p.next = node
        node.prev = self.right_p

        self.right_p = node
        node.next = None

        if self.left_p is None:
            self.left_p = node
            self.head.next = node