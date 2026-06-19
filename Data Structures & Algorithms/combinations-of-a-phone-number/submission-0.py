class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        hash = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
            }

        res = []

        def backtrack(idx, sub):
            if idx == len(digits):
                res.append(sub)
                return 
            
            subs = hash[digits[idx]]
            
            for ch in subs:
                backtrack(idx+1, sub+ch)

        backtrack(0, "")
        return res