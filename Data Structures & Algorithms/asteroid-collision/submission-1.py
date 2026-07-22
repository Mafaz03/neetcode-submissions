class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            stack.append(num)

            while (len(stack) > 1) and (stack[-1] < 0 and stack[-2] > 0):
                if abs(stack[-1]) > abs(stack[-2]):
                    to_add = stack.pop()
                    stack.pop()
                    stack.append(to_add)
                elif abs(stack[-1]) < abs(stack[-2]):
                    stack.pop()
                    to_add = stack.pop()
                    stack.append(to_add)
                else:
                    stack.pop()
                    stack.pop()

        return stack