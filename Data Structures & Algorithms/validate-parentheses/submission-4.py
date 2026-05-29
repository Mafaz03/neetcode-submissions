class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n % 2 != 0: return False

        brac = {")": "(", "]": "[", "}": "{"}

        open_brac  = set(["(", "[", "{"])
        close_brac = set([")", "]", "}"])

        for i in s:
            
            if i in close_brac:
                if len(stack) == 0: return False
                if stack[-1] == brac[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False