class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            print("wow")
            return 0
        
        nums = set(nums)
        maximum = max(nums)

        max_seqs = []
        max_seq  = 0

        for i in range(min(nums), maximum+1):
            if i in nums:
                max_seq += 1
                if i == maximum:
                    max_seqs.append(max_seq)
            else:
                # print(max_seq)
                max_seqs.append(max_seq)
                max_seq = 0
        
        return max(max_seqs) if len(max_seqs) != 0 else len(nums)
