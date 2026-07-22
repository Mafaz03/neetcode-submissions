class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for chr in s:
            if chr.isdigit(): 
                # chr = int(chr)
                if stack and stack[-1].isdigit():
                    dig = stack.pop()
                    chr = str(dig) + str(chr)
            print(stack)
            if chr == "]":
                to_add = ""
                while stack[-1] != "[":
                    ele = stack.pop()
                    to_add = ele + to_add
                stack.pop()
                chr = int(stack.pop()) * to_add
                to_add = ""

            stack.append(chr)

        return ''.join(stack)