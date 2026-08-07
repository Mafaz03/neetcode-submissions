class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        
        visited = set(deadends)

        dq = deque(['0000'])

        steps = 0

        while dq:
            for _ in range(len(dq)):
                combination = dq.popleft()
                if combination == target: 
                    return steps + 1

                visited.add(combination)
                digits = [int(combination[i]) for i in range(4)]

                for d in range(4):
                    for a_s in [1, -1]:
                        digits_copy = digits.copy()
                        digits_copy[d] = (digits[d] + a_s) % 10

                        new_combination = "".join([str(i) for i in digits_copy])
                        if new_combination not in visited:
                            print(new_combination)
                            visited.add(new_combination)
                            if new_combination == target: 
                                return steps + 1
                            else:
                                dq.append(new_combination)
            steps += 1
        return -1