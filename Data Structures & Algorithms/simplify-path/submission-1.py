class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        to_add = ""

        for p in path + "/":    
            if p != "/":
                to_add += p
            else:
                if to_add:
                    
                    if to_add == ".":
                        to_add = ""
                        continue
                    elif to_add == ".." and len(stack) == 0:
                        to_add = ""
                        continue
                    elif to_add == ".." and len(stack) > 0:
                        stack.pop()
                    else: 
                        stack.append(to_add)
                    
                    to_add = ""
        return '/'+'/'.join(stack)