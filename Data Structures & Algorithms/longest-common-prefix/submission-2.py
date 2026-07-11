class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word_idx in range(1, len(strs)):
            curr_word = strs[word_idx]
            if curr_word == "":
                return ""
            
            mismatch = False
            for w_idx in range(min(len(curr_word), len(prefix))):
                if curr_word[w_idx] != prefix[w_idx]:
                    mismatch = True
                    print(w_idx)
                    prefix = prefix[:w_idx]
                    if prefix == "":
                        return ""
                    break
            if not mismatch:
                prefix = prefix[:len(curr_word)]

        return prefix

