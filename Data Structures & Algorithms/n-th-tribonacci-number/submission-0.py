class Solution:
    def tribonacci(self, n: int) -> int:
        Tn0 = 0
        Tn1 = 1
        Tn2 = 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        for _ in range(n-2):
            Tn0, Tn1, Tn2 = Tn1, Tn2, Tn0 + Tn1 + Tn2
            # print(Tn0)
            # print(Tn1)
            print(Tn2)
        return Tn2

        