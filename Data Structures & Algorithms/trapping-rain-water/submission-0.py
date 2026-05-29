class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        max_L = 0
        maxes_L = []

        max_R = 0
        maxes_R = []

        maxes_L.append(0)
        maxes_R.append(0)

        for i in range(1, n):
            max_L = max(height[i-1], max_L)
            maxes_L.append(max_L)

        for i in range(2, n+1):
            index = -1 * i
            max_R = max(height[index+1], max_R)
            maxes_R.append(max_R)

        water_amounts = 0
        for i in range(n):
            water_amount = max((min(maxes_L[i], maxes_R[n - i - 1]) - height[i]), 0)
            water_amounts += water_amount
            print(water_amount)

        return water_amounts
