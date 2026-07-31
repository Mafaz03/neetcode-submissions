class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp_nums = []
        res = []

        def backtrack(num):

            if len(temp_nums) == k:
                res.append(temp_nums.copy())

            for i in range(num, n + 1):
                temp_nums.append(i)
                backtrack(i + 1)
                temp_nums.pop()
            
        backtrack(1)
        return res