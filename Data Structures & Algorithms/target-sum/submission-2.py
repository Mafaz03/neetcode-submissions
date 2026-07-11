class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if target > sum(nums): return 0
        prev_row = [0] * ((sum(nums)*2)+1)
        prev_row[0 + sum(nums)] = 1
        
        for idx in range(len(nums)):
            curr_row = [0] * ((sum(nums)*2)+1)

            for i, j in enumerate(prev_row):
                if j != 0:
                    # if i + nums[idx] < len(curr_row):
                    curr_row[i + nums[idx]] += j

                    # if i - nums[idx] >= 0:
                    curr_row[i - nums[idx]] += j

            print(curr_row)
            prev_row = curr_row

        return curr_row[target+sum(nums)]