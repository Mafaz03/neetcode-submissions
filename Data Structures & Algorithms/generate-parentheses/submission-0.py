class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def paraBack(brac: str, open: int, close: int):
            if len(brac) == (2 * n):
                res.append(brac)
                return
            
            if open < n:
                paraBack(brac + "(", open + 1, close)
            
            if open > close:
                paraBack(brac + ")", open, close + 1)

        paraBack("", 0, 0)

        return res