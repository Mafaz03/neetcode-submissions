"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times   = sorted([i.end for i in intervals])


        count = 0
        max_count = 0

        while start_times:
            if start_times[0] < end_times[0]:
                count += 1
                start_times = start_times[1:]
            # elif start_times[0] >= end_times[0]:
            else:
                count -= 1
                end_times = end_times[1:]
            max_count = max(max_count, count)
            print(count)

        return max_count