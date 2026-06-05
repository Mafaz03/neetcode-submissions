class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.append(set())
        while type(nums[0]) != set:
            # print(nums, nums[0])
            print(nums)
            if nums[0] in nums[-1]:
                return nums[0]
            
            nums[-1].add(nums[0])
            nums = nums[1:]