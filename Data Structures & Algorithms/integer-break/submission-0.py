class Solution:
    def integerBreak(self, n: int) -> int:
        def breakup(num):
            a = 0
            b = num

            res = []

            for _ in range(b-1):
                a += 1
                b -= 1

                res.append([a,b])

            return res

        mem = {}

        def dfs(num):

            if num == 1:
                return 1

            if num in mem:
                return mem[num]
            
            broke = breakup(num)

            ans = float("-inf")

            for a, b in broke:
                print(a, b)

                left  = max(a, dfs(a))
                right = max(b, dfs(b))

                ans = max(ans, left * right)

                mem[num] = ans

            return ans

        return dfs(n)