class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        ops = set(["+", "-", "*", "/"])

        for num_or_op in tokens:
            if num_or_op.lstrip('-').isdigit():
                stack.append(int(num_or_op))

            elif num_or_op in ops:
                if num_or_op == "+":
                    new_val = stack[-2] + stack[-1]
                elif num_or_op == "-":
                    new_val = stack[-2] - stack[-1]
                elif num_or_op == "*":
                    new_val = stack[-2] * stack[-1]
                elif num_or_op == "/":
                    new_val = int(stack[-2] / stack[-1])
                    
                
                stack.pop()
                stack.pop()

                stack.append(new_val)

            # print(stack)
        
        return stack[-1]
