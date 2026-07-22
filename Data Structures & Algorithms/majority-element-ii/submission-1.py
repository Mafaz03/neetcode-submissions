class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()

        nums.sort()

        criteria = len(nums)//3

        prev_elemnet = nums[-1]

        count = 0

        while nums:
            element = nums.pop()
            if element == prev_elemnet:
                count += 1
            else:
                count = 1

            if count > criteria:
                # print(element, count)
                ans.add(element)

            # print(count)
            
            prev_elemnet = element
        
        return list(ans)