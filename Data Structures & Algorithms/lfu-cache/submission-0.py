from collections import defaultdict

class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.map = {}

        self.LeftNode = Node(0)
        self.RightNode = Node(0)

        self.LeftNode.next = self.RightNode
        self.RightNode.prev = self.LeftNode

    def length(self):
        return len(self.map)

    def pushRight(self, key):
        node = Node(key, self.RightNode.prev, self.RightNode)
        self.map[key] = node

        node.prev.next = node
        self.RightNode.prev = node

    def pop(self, key):
        if key not in self.map:
            return

        node = self.map.pop(key)

        node.prev.next = node.next
        node.next.prev = node.prev

    def popLeft(self):
        if self.length() == 0:
            return None

        key = self.LeftNode.next.key
        self.pop(key)
        return key


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.least_count = 0

        self.key_val_hash = {}                 # key -> value
        self.key_count_hash = defaultdict(int) # key -> freq
        self.count_ll_hash = defaultdict(DoublyLinkedList) # freq -> DLL

    def counter(self, key):
        count = self.key_count_hash[key]

        # remove from old frequency list
        if count > 0:
            self.count_ll_hash[count].pop(key)

            if count == self.least_count and self.count_ll_hash[count].length() == 0:
                self.least_count += 1

        # add to new frequency list
        self.key_count_hash[key] = count + 1
        self.count_ll_hash[count + 1].pushRight(key)

    def get(self, key: int) -> int:
        if key not in self.key_val_hash:
            return -1

        self.counter(key)
        return self.key_val_hash[key]

    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return

        # key already exists
        if key in self.key_val_hash:
            self.key_val_hash[key] = value
            self.counter(key)
            return

        # cache full
        if len(self.key_val_hash) == self.cap:
            evict = self.count_ll_hash[self.least_count].popLeft()

            self.key_val_hash.pop(evict)
            self.key_count_hash.pop(evict)

        # insert new key
        self.key_val_hash[key] = value
        self.key_count_hash[key] = 0
        self.counter(key)

        self.least_count = 1