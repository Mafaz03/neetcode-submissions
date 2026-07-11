class Solution:
    def maxProduct(self, nums: List[int]) -> int:
 
        max_prod = min_prod = ans = nums[0]

        for i in range(1, len(nums)):
            
            max_prod, min_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i]), min(max_prod * nums[i], min_prod * nums[i], nums[i])
            ans = max(max_prod, ans)

        return ans