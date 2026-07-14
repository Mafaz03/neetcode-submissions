class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hash = [Node(-1,-1) for _ in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        hash_key = key % 1000
        dummy    = self.hash[hash_key]

        while dummy:
            if dummy.key == key:
                dummy.value = value
                return 

            if dummy.next == None:
                dummy.next = Node(key, value)
                return

            dummy = dummy.next


    def get(self, key: int) -> int:
        hash_key = key % 1000
        dummy    = self.hash[hash_key]

        while dummy:
            if dummy.key == key:
                return dummy.value
            dummy = dummy.next
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = key % 1000
        dummy = self.hash[hash_key]
        
        while dummy.next:
            if dummy.next.key == key:
                dummy.next = dummy.next.next
                return
            dummy = dummy.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)








