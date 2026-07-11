class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        end_val = intervals[0][1]

        for interval in intervals:
            if (not res) or (res[-1][1] <= interval[0]):
                res.append(interval)
            else:
                end_val = min(res[-1][1], interval[1])
                res[-1][1] = end_val

        # print(intervals)
        # print(res)
        return len(intervals) - len(res)