"""
252. Meeting Rooms
Easy

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

###############################################################################
"""
Solution: sort intervals. Check if adjacent intervals overlap.

Assume the person has to attend each meeting in full. Then the person can
attend all meetings if and only if no intervals overlap (other than
trivially at a point.)

O(n log n) time: for sorting
O(1) extra space
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort()
        
        for i in range(1, n):
            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True
