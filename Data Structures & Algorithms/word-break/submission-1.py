class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def match(s, tgt, start_idx):
            return s.startswith(tgt, start_idx)

        mem = {}

        def backtrack(i):
            if i == len(s):
                return True

            if i in mem:
                return mem[i]
            for w in wordDict:
                if match(s, w, i):
                    if backtrack(i+len(w)):
                        mem[i] = True
                        return True
                        
            mem[i] = False
            return False

        return backtrack(0)