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
            
        intervals.sort(key=lambda x: x.start)
        
        free_rooms = []
        for interval in intervals:
            if free_rooms and free_rooms[0] <= interval.start:
                heapq.heappop(free_rooms)
        
            heapq.heappush(free_rooms, interval.end)
        
        return len(free_rooms)
