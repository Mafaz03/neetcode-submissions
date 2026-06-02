class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0

        queue = deque()

        results = []

        while r < len(nums):

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r-l+1) == k:
                results.append(nums[queue[0]])
                l += 1
            r += 1

        return results