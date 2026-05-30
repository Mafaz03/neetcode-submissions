class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        # print(self.stack)
        self.stack.append(val)
        if (self.minimum_stack == []):
            self.minimum_stack.append(val)

        elif self.minimum_stack[-1] < val:
            self.minimum_stack.append(val)
        

    def pop(self) -> None:
        # print(self.stack)
        self.stack.pop()
        if len(self.minimum_stack) > 1 and len(self.stack) > 1:
            if self.stack[-1] == self.minimum_stack[-1]:
                self.minimum_stack.pop()
        

    def top(self) -> int:
        # print(self.stack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print(self.stack)
        return min(self.stack)
        
