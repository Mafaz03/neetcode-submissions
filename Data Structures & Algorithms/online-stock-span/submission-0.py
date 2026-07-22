class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span  = []
        

    def next(self, price: int) -> int:
        
        count = 0
        while (self.stack) and self.stack[-1] <= price:
            self.stack.pop()
            count += self.span.pop()
        
        self.stack.append(price)
        self.span.append(count+1)

        return count+1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)