class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n = len(s1)
        m = len(s2)

        s1_alpha_list = [0] * 26
        s2_alpha_list = [0] * 26

        for i in range(n):
            s1_alpha_list[ord(s1[i]) - 97] += 1
            s2_alpha_list[ord(s2[i]) - 97] += 1
            

        if s1_alpha_list == s2_alpha_list:
            return True

        for i in range(n,m):
            s2_alpha_list[ord(s2[i]) - 97] += 1
            s2_alpha_list[ord(s2[i-n]) - 97] -= 1

            if s1_alpha_list == s2_alpha_list:
                return True
        return False