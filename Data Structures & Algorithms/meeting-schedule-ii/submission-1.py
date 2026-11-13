"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
When do we need a meeting room, if all meetings in the day are sorted by start time? 
1. Each meeting will require at least 1 room, but that room could be shared if there are no overlaps with the next meeting. 
    * Predicate: If the start time of a meeting ends before the next starts, then a room can be shared. We should while loop through the heap if we continue finding cases where there's no overlap so that we don't double count meeting rooms. 
2. If the meeting that starts before the next has an end time greater than the start time of the next, then there is a conflict. 
    * Predicate: If the end time of a meeting is greater than the start time of the next, the meeting rooms of these 2 meetings can't be shared. So. 2 separate meeting rooms are needed for both of the rooms. We should account for this by 
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        end_time_heap = []
        intervals.sort(key=lambda x: x.start)
        
        heapq.heappush(end_time_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            meeting = intervals[i]

            earliest_active_meeting_en = end_time_heap[0]

            # If the earliest active meeting ends before the current meeting start, we can use the same room. Pop that meeting end time off of the heap. 
            if earliest_active_meeting_en <= meeting.start:
                heapq.heappop(end_time_heap)
            
            heapq.heappush(end_time_heap, meeting.end)
        
        return len(end_time_heap)