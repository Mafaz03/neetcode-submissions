class Node:
    def __init__(self, val, next = None):
        self.val  = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.capacity = 0

        self.front = Node(0)
        self.rear  = self.front

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.k: return False

        self.rear.next = Node(value)
        self.rear = self.rear.next
        self.capacity += 1
        
        return True

    def deQueue(self) -> bool:
        if self.capacity == 0: return False

        self.front = self.front.next
        self.capacity -= 1
        return True

    def Front(self) -> int:
        if self.capacity == 0: return -1
        return self.front.next.val
        
    def Rear(self) -> int:
        if self.capacity == 0: return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.capacity == 0
        
    def isFull(self) -> bool:
        return self.capacity == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()