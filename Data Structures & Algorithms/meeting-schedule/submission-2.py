"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for i in range(len(intervals)-1):
            previous = intervals[i]
            after = intervals[i+1]

            if previous.end > after.start and previous.start < after.end:
                return False
        return True