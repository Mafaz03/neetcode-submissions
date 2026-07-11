"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def start_sort(x):
            return x.start

        intervals = sorted(intervals, key = start_sort)

        for idx, interval in enumerate(intervals):
            if idx != len(intervals)-1:
                if intervals[idx].end > intervals[idx+1].start:
                    return False
        return True