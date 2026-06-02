class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        maxes = []
        window = nums[:k]

        max_index, max_value = max(enumerate(window), key = lambda x: x[1])
        maxes.append((max_value, max_index))
        print(window, maxes)

        for i in range(1, n-k+1):

            window = nums[i: i+k]


            old_max, old_max_idx = maxes[-1]

            if old_max_idx == 0:
                max_index, max_value = max(enumerate(window), key = lambda x: x[1])
            else:
                max_index, max_value = max(enumerate([old_max, nums[i+k-1]]), key = lambda x: x[1])

            maxes.append((max_value, max_index))
        
        return [i[0] for i in maxes]