class CountSquares:

    def __init__(self):
        self.counter = Counter()
        

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        
        x1, y1 = point
        count = 0

        for diagnol in self.counter:
            x2, y2 = diagnol

            if (abs(x1 - x2) == abs(y1 - y2)) and (x1 != x2 or y1 != y2):

                if ((x1, y2) in self.counter) and ((x2, y1) in self.counter):
                    count += self.counter[(x1, y2)] * self.counter[(x2, y1)] * self.counter[(x2, y2)]

        return count 

            
        








