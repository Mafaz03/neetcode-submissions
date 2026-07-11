class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)//2

        if (sum(nums)/2 - target) != 0: return False
        

        combination_sum = set()
        combination_sum.add(0)
        combination_sum.add(nums[-1])

        for i in range(len(nums)-2, -1, -1):
            for j in combination_sum.copy():
                combination_sum.add(j + nums[i])
                if target in combination_sum: return True
        
        return False