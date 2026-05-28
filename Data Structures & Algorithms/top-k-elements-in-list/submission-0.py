from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        numbers = counter.keys()
        freqs   = counter.values()

        # bucket sort
        ddict = defaultdict(list)
        maximum = max(freqs)
        n = len(freqs)
        for i in freqs:
            normalised = i / (maximum + 1)
            bucket_no  = int(n * normalised)
            ddict[bucket_no].append(i)
        
        values = []
        freq_list    = list(freqs)
        numbers_list = list(numbers)
        for bucket in range(n-1, -1, -1):
            # print(bucket)
            if bucket in ddict:
                values_sorted = sorted(ddict[bucket]) # sort bucket's freq
                print(values_sorted)
                for f in values_sorted:
                    index = freq_list.index(f)
                    values.append(numbers_list[index])

                    freq_list.pop(index)
                    numbers_list.pop(index)

                    if len(values) == k: return values
        
        return values
