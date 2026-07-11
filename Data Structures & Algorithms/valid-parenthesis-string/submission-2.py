class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMin = 0
        leftMax = 0

        for b in s:
            if b == "(":
                leftMin += 1
                leftMax += 1
            
            elif b == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0: return False

            leftMin = max(leftMin, 0)
        return leftMin == 0

