class MyStack:

    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
        

    def push(self, x: int) -> None:
        if len(self.queue1) != 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
        
    def pop(self) -> int:
        q1 = self.queue1 if self.queue1 else self.queue2
        q2 = self.queue2 if self.queue1 else self.queue1

        while len(q1) > 1:
            q2.append(q1.popleft())

        return q1.popleft()

    def top(self) -> int:
        if len(self.queue1) != 0:
            return self.queue1[-1]
        else:
            return self.queue2[-1]
        
    def empty(self) -> bool:
        if len(self.queue1) + len(self.queue2) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()