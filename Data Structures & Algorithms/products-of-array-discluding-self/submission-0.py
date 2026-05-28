class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        L = []
        R = []

        L.append(1)
        R.append(1)


        for i in range(1, len(nums)):
            L.append(nums[i-1] * L[i-1])


        for i in range(len(nums)-1, 0, -1):
            R.append(R[len(nums)-i-1] * nums[i])

        prod = []
        for i in range(len(R)-1, -1, -1):
            prod.append(L[len(nums)-i-1] * R[i])

        return prod