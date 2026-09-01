class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        min_length = min(len(str1), len(str2))

        for i in range(min_length, 0, -1):
            if (len(str1) % i != 0) or (len(str2) % i != 0):
                continue

            sub_str1 = str1[: i]
            sub_str2 = str2[: i]

            if sub_str1 != sub_str2: continue

            
            to_mul_1 = len(str1) // i
            to_mul_2 = len(str2) // i
            # print(sub_str1, to_mul_1, sub_str2, to_mul_2)
            if ((sub_str1 * to_mul_1) == str1) and ((sub_str2 * to_mul_2) == str2):
                return sub_str1
            
        return ""
            