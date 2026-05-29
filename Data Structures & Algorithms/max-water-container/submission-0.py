class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0

        l = 0
        r = len(heights)-1

        while l < r:
            
            
            max_vol = max(max_vol, abs(l-r) * min(heights[l], heights[r]))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return  max_vol