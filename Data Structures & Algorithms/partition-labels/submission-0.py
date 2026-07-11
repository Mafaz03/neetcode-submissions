class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter_hash = Counter(s)

        res = []

        idx_1 = 0
        idx = 0

        while idx < len(s):
            in_use = {s[idx]}
            while len(in_use) != 0:
                in_use.add(s[idx])
                counter_hash[s[idx]] -= 1
                if counter_hash[s[idx]] == 0: in_use.remove(s[idx])
                idx += 1

            res.append(idx-idx_1)
            idx_1 = idx
        return res