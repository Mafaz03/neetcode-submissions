class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        pt1 = 0
        pt2 = 0

        while pt1 < len(word1) and pt2 < len(word2):
            new_str += word1[pt1]
            new_str += word2[pt2]

            pt1 += 1
            pt2 += 1
        
        if len(word1) > len(word2): # word1 left over
            new_str += word1[pt1:]

        if len(word1) < len(word2): # word2 left over
            new_str += word2[pt2:]
        
        return new_str