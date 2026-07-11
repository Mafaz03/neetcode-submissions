class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []


        for i in range(n+1):

            temp_i = i
            count = 0

            for _ in range(32):
                if temp_i % 2 == 1: 
                    count += 1
                temp_i = temp_i >> 1
                
            res.append(count)

        return res