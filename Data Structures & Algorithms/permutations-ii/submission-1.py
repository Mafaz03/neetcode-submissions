class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, idxs: set):

            if len(path) == len(nums):
                res.append(path.copy())
                return

            for idx_2, i in enumerate(range(0, len(nums))):
                if (i > 0) and (nums[i] == nums[i-1]) and (i-1 in idxs):
                    continue

                if idx_2 not in idxs:
                    path.append(nums[i])
                    idxs.add(idx_2)

                    backtrack(path, idxs)
                    
                    idxs.remove(idx_2)
                    path.pop()
                    
        backtrack([], set())
        return res