class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = {}
        t_dict = {}

        for idx in range(len(s)):
            if s[idx] in s_dict: s_dict[s[idx]] += 1
            else: s_dict[s[idx]] = 1

            if t[idx] in t_dict: t_dict[t[idx]] += 1
            else: t_dict[t[idx]] = 1

        return s_dict == t_dict