class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                poped_temp, poped_idx = stack.pop()
                result[poped_idx] = idx - poped_idx
            stack.append((temp, idx))
        return result
            