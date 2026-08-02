class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def match(word: str, prefix_word: str, start_idx: int):
            return word.startswith(prefix_word, start_idx)

        result = []

        mem = {}

        def backtrack(i, temp_res: list):
            if i == len(s):
                result.append(" ".join(temp_res))
                return 
            
            # if i in mem:
            #     return mem[i]

            for w in wordDict:
                if match(s, w, i):
                    temp_res.append(w)
                    backtrack(i+len(w), temp_res)
                    temp_res.pop()
            
                    # mem[i] = temp_res

        backtrack(0, [])
        return result