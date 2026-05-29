class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sol = []

        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                target = -(nums[i] + nums[j])
                if target in nums[j+1:]: 
                    # ordering
                    a = nums[i]
                    b = nums[j]
                    c = target
                    sub = sorted([a, b, target])
                    if sub not in sol: sol.append(sub)
        return sol