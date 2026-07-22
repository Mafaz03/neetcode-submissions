class FreqStack:

    def __init__(self):
        self.group_mapper = defaultdict(list) # {count: [elements]}
        self.counter = defaultdict(int)       # {elements: count}

        self.maxx = 0
        
    def push(self, val: int) -> None:

        self.counter[val] += 1
        self.maxx = max(self.maxx, self.counter[val])

        self.group_mapper[self.counter[val]].append(val)

    def pop(self) -> int:

        
        element = self.group_mapper[self.maxx].pop()
        self.counter[element] -= 1

        if len(self.group_mapper[self.maxx]) == 0:
            self.maxx -= 1

        return element
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()