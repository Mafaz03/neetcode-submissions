def checkPalindrome(word: str):
    if len(word) == 1: return True

    p_s = 0
    p_e = len(word)-1

    while p_e >= p_s:
        if word[p_e] != word[p_s]:
            return False
    
        p_e -= 1
        p_s += 1
        
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                sub = s[start: end+1]
                if checkPalindrome(sub):
                    path.append(sub)
                    dfs(end+1, path)
                    path.pop()
            
        dfs(0, [])
        return res


















