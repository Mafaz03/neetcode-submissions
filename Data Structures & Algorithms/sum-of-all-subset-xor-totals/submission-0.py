class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        temp_nums = []
        summ = [0]

        def backtracking(idx):

            res = 0
            for i in temp_nums: res ^= i
            summ[0] += res

            for i in range(idx, len(nums)):
                temp_nums.append(nums[i])
                backtracking(i+1)
                temp_nums.pop()

        backtracking(0)
        return summ[0]