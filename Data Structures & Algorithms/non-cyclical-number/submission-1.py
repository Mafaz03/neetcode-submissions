class Solution:
    def isHappy(self, n: int) -> bool:
        temp_n = 0

        visited = set()

        while temp_n != 1:
            while n:
                digit = n % 10
                n = n // 10
                temp_n += digit**2

            # print(temp_n)
            if temp_n == 1:
                return True
                
            if temp_n in visited:
                return False

            visited.add(temp_n)
            n = temp_n
            temp_n = 0
