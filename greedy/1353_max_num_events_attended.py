"""
1353. Maximum Number of Events That Can Be Attended
Medium

Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:

Input: events = [[1,100000]]
Output: 1

Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
"""

from typing import List
import heapq


###############################################################################
"""
Solution: sort by start times (then end times), but do in reverse so we
can pop earlier events from the end of the list.  Use min heap of end times.
Remove events that have already ended.  Then greedily attend events that
end soonest.

Each day is only considered once.  Each event is pushed once and popped once.

O(n log n) time, where n = number of events, due to sorting.  Loop is O(n).

O(n) extra space: for heap, in case all n events end as late as possible.
Then they stay on the heap until we choose to attend them one by one.

*** This is a good solution, despite the relatively slow runtime on LC.
LC doesn't have enough good test cases.

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue

Runtime: 912 ms, faster than 74.37% of Python3 online submissions
Memory Usage: 47.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def maxEvents(self, events: List[List[int]]) -> int:
		# Sort in reverse so we can remove the earliest events by popping
		# them from the end of the list, which costs O(1) time.
		events.sort(reverse=True)
		
		h = [] # min heap of end times
		count = 0 # number of events attended

		# number of events left to consider; used to break loop early
		n_events = len(events)

		for day in range(1, 100001): # today
			# Remove events that start on or before today from the list and 
			# add their end times to the heap.
			while events and events[-1][0] <= day:
				heapq.heappush(h, events.pop()[1])
				n_events -= 1

			# Remove events (ending times) from the heap that already 
			# ended (before today).
			while h and h[0] < day:
				heapq.heappop(h)

			# Attend the event that is currently ongoing (starting today or 
			# has already started) and has the earliest end time.
			if h:
				heapq.heappop(h)
				count += 1
			elif n_events <= 0:
				break

		return count

"""
Solution 1b: same as sol #1, but only consider days for which there are
events, instead of iterating through all possible days.

O(n log n): sorting dominates the O(n) part.  The loop is O(n) since days
are only incremented or set as needed.

O() extra space

Runtime: 848 ms, faster than 90.97% of Python3 online submissions
Memory Usage: 47.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
	def maxEvents(self, events: List[List[int]]) -> int:
		# Sort in reverse so we can remove the earliest events by popping
		# them from the end of the list, which costs O(1) time.
		events.sort(reverse=True)
				
		h = [] # min heap of end times
		count = 0

		while events or h:
			# If there are events still on the heap, ie, the events have
			# started but not yet ended, then we already incremented day by 1.
			# Otherwise, the heap is empty, so we consider the start day
			# of the next earliest event.
			if not h:
				day = events[-1][0]

			# Remove events that start on or before today from the list and 
			# add their end times to the heap.
			while events and events[-1][0] <= day:
				heapq.heappush(h, events.pop()[1])

			# Remove events (ending times) from the heap that already 
			# ended (before today).
			while h and h[0] < day:
				heapq.heappop(h)

			# Attend the event that is currently ongoing (starting today or 
			# has already started) and has the earliest end time.
			if h:
				heapq.heappop(h)
				count += 1
				day += 1

		return count

###############################################################################
"""
Solution 2: sort by end times, and use set to store which days have been
used to attend an event.  Going through events, starting with those
ending earlier, pick the first day available to attend.

*** SLOW when there are a huge number of events that overlap, in which case
many of the same days are looped through.  LC doesn't have enough good test 
cases.

O(nd + n log n) time, where n = number of events, d = number of possible days.
The O(n log n) is for sorting.

O(d) extra space: for set.  Assume sorting events in-place.

Runtime: 800 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 50.5 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def maxEvents(self, events: List[List[int]]) -> int:
		events.sort(key=lambda x: x[1])
		#print(f"\nsorted = {events}")

		used = set() # days that have been used to attend an event

		for start, end in events:
			for d in range(start, end + 1):
				if d not in used:
					used.add(d)
					break

		return len(used)

###############################################################################

if __name__ == "__main__":
	def test(events, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\nevents = {events}")

		res = sol.maxEvents(events)

		print(f"\nres = {res}")


	sol = Solution()
	#sol = Solution1b()
	#sol = Solution2()
	
	comment = "LC ex1; answer = 3"
	events = [[1,2],[2,3],[3,4]]
	test(events, comment)

	# 2, 3, 4, 1
	comment = "LC ex2; answer = 4"
	events= [[1,2],[2,3],[3,4],[1,2]]
	test(events, comment)

	# x, 4, 2, 3.x, 1
	comment = "LC ex3; answer = 4"
	events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
	test(events, comment)

	comment = "LC ex4; answer = 1"
	events = [[1,100000]]
	test(events, comment)

	comment = "LC ex5; answer = 7"
	events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
	test(events, comment)

	comment = "LC test case; answer = 3"
	events = [[1,2],[1,2],[1,6],[1,2],[1,2]]
	test(events, comment)

	comment = "LC test case; answer = 5"
	events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
	test(events, comment)

	comment = "LC test case; answer = 5"
	events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
	test(events, comment)

	comment = "LC test case; answer = 4"
	events = [[1,3],[1,3],[1,3],[3,4]]
	test(events, comment)

	comment = "LC test case; answer = 2"
	events = [[1,10],[2,2],[2,2],[2,2],[2,2]]
	test(events, comment)

	comment = "LC test case; answer = 5"
	events = [[7,11],[7,11],[7,11],[9,10],[9,11]]
	test(events, comment)

	comment = "LC test case; answer = 18"
	events = [[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],[7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]]
	test(events, comment)

	# comment = "Huge number of events"
	# events = [[1, i] for i in range(10000)]
	# test(events, comment)
