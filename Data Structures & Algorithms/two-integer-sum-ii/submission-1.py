class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dict = {numbers[i]: i for i in range(len(numbers))}
        sol = []

        minimum = numbers[0]
        maximum = numbers[-1]

        for i in range(len(numbers)):
            desired = target - numbers[i]
            # print(desired)
            if desired in numbers_dict and desired != numbers[i]: 
                if desired < numbers[i]:
                    sol = [numbers_dict[desired]+1, i+1]
                else:
                    sol = [numbers[i], numbers_dict[desired]+1]
        return sol
