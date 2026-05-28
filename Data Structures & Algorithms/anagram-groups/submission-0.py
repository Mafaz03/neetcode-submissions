from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict = defaultdict(list)
        for s in strs:
            ddict["".join(sorted(s))].append(s)
        return list(ddict.values())