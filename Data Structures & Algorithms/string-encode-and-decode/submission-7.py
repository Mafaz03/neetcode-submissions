class Solution:

    def encode(self, strs) -> str:
        # if len(strs) == 0: return ['']
        
        nums = ""
        s = ""
        for i in range(len(strs)):
            nums += str(len(strs[i])) + "~"
            s += strs[i]
        return nums + s


    def decode(self, s: str) -> List[str]:
        idx = []
        for i in s.split("~")[:-1]:
            idx.append(int(i))
        

        only_str = s.split("~")[-1]

        words = []
        for i in idx:
            word = only_str[: i]
            only_str = only_str[i: ]
            words.append(word)

        return words

