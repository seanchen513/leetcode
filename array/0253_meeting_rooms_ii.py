"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

###############################################################################
"""
Solution 1: use sorting and a counter.

When a meeting (interval) starts, a new room is needed (possibly a previous
used one).  When a meeting (interval) ends, the room used is now available.
A room counter keeps track of how many rooms are being used at each moment.
The counter is incremented when a meeting starts, and decremented when a 
meeting ends.

Assume: If a meeting starts exactly when another ends, the room taken up
by the ending meet will be made free first.  In the solution, this corresponds 
to having start == end, but (end, -1) < (start, 1) so the ending meeting
is processed first.

O(n log n) time for sorting
O(n) extra space for "s" array
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s = sorted([(start, 1) for start, end in intervals] + 
            [(end, -1) for start, end in intervals])

        count = 0 # how many rooms are open
        max_count = 0

        for _, effect in s:
            count += effect
            max_count = max(max_count, count)

        return max_count

###############################################################################
"""
Solution 2: use sorting and a min heap of end times.

O(n log n) time: for sorting, and for O(n) heap pops and pushes, each of
which is an O(log n) operation.

O(n) extra space: for sorted array (if not modifying given array), and
for heap.
"""
class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        import heapq

        s = sorted(intervals) # sorted by start time first, then by end time

		# min heap of end times of meetings, or when the room frees up
        rooms = [s[0][1]] # start with end time of first meeting

        for i in range(1, len(s)):
            # If the first room to free up does so before or at the same time
            # as the next meeting waiting for a room, make the room available.
            if rooms[0] <= s[i][0]: 
                heapq.heappop(rooms)

            heapq.heappush(rooms, s[i][1]) # start the current meeting

		# Note: we free up only the rooms required to hold new meetings.
		# Some meetings might have already ended, but they are still in the
		# heap.  The heap only grows in size, and stays the same size once
		# it reaches the maximum number of rooms required.

		# If we wanted to free up all rooms possible, we could change the 
		# "if" within loop to a nested loop, freeing all the rooms whose 
		# meetings have ended.  Then we would need to keep track of the max 
		# size of the heap.

        return len(rooms)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{arr}")
        
        res = s.minMeetingRooms(arr)

        print(f"\nresult = {res}")


    s = Solution() # sorting and counter
    s = Solution2() # sorting and heap

    comment = "LC ex1; answer = 2"
    arr = [[0, 30],[5, 10],[15, 20]]
    test(arr, comment)

    comment = "LC ex2; answer = 1"
    arr = [[7,10],[2,4]]
    test(arr, comment)

    comment = "telescoping"
    arr = [[0,10], [1,9],[2,8],[3,7],[4,6],[11,12]]#,[,],[,],[,]]
    test(arr, comment)
    