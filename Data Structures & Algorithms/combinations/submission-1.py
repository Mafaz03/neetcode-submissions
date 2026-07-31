class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(temp_nums, num):

            if len(temp_nums) == k:
                res.append(temp_nums.copy())
                return

            for i in range(num, n + 1):
                temp_nums.append(i)
                backtrack(temp_nums, i + 1)
                temp_nums.pop()
            
        backtrack([], 1)
        return res