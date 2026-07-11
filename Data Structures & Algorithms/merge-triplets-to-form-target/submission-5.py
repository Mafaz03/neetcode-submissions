class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set() # should be {0,1,2}

        for t in triplets:
            if (t[0] > target[0]) or (t[1] > target[1]) or (t[2] > target[2]):
                continue
            
            for idx, t_val in enumerate(t):
                if t_val == target[idx]:
                    good.add(idx)
        return len(good) == 3