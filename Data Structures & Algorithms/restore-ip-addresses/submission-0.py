class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def check_valid(ss: str, points: int):
            for s in ss.split(".")[:points]:
                if not s:
                    return False

                i = int(s)

                if not (str(i) == s and 0 <= i <= 255):
                    return False

            return True
        
        res = [set()]

        def backtrack(s, dots_count, idx):
            # print(s)
            if (dots_count == 3) and (len(s.split(".")) == 4) and (check_valid(s, 4)):
                res[0].add(s)
                return
            
            if idx == len(s):
                return
            
            # add dot at idx
            # print(s[:idx+1] + "." + s[idx+1:], dots_count)
            if check_valid(s[:idx+1] + "." + s[idx+1:], dots_count+1):
                backtrack(s[:idx+1] + "." + s[idx+1:], dots_count + 1, idx + 2)

            # dont add dot at idx and skip
            backtrack(s, dots_count, idx + 1)
        backtrack(s, 0, 0)
        return list(res[0])