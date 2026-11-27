"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x.start)
        minheap = [intervals[0].end]
        heapq.heapify(minheap)

        for i in range(1, len(intervals)):
            if minheap[0] > intervals[i].start:
                heapq.heappush(minheap, intervals[i].end)
            else:
                min_end = heapq.heappop(minheap)
                heapq.heappush(minheap, max(min_end, intervals[i].end))
        return len(minheap)
