class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hash = [Node(-1) for _ in range(10**4)]
        

    def add(self, key: int) -> None:
        hash_key = key % 10**4
        d = self.hash[hash_key]
        
        found = False

        while d:
            if d.val == key:
                return 
            if d.next == None:
                d.next = Node(key)
            d = d.next
            

    def remove(self, key: int) -> None:
        hash_key = key % 10**4
        d = self.hash[hash_key]

        while d.next:
            if d.next.val == key:
                d.next = d.next.next
                return
            d = d.next
        

    def contains(self, key: int) -> bool:
        hash_key = key % 10**4
        d = self.hash[hash_key]

        while d:
            if d.val == key:
                return True
            d = d.next
        return False


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)