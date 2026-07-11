class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, n):
            if n == 0:
                return 1
            
            res = 1
            if n % 2 == 0:
                a = recursion(x, n/2)
                res = a * a
            else:
                a = recursion(x, n//2)
                res = a * a * x

            return res
        if n < 0:
            x = 1/x
            n = -1 * n
        
        return recursion(x,n)