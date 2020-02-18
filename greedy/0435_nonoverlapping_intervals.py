"""
435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

from typing import List

###############################################################################
"""
Solution 1: Greedy algo.  Sort intervals by starting endpoint.  Keep count of
number of intervals discarded.

Check if adjacent intervals overlap.  If they do, keep the one with the 
smaller right endpoint.

O(n log n): due to sorting.  Loop is O(n).
O(1) extra space: for in-place sort.
"""
class Solution:
	def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
		if not a:
			return 0
		
		a.sort()
		
		n = len(a)
		count = 0 # number of intervals discarded
		last_endpt = a[0][1]
		
		for i in range(1, n):
			if a[i][0] < last_endpt: # overlap
				count += 1
				last_endpt = min(last_endpt, a[i][1])
			else:
				last_endpt = a[i][1]
				
		return count

###############################################################################
"""
Solution 2: Greedy algo.  Sort intervals by right endpoint.  Keep count of
number of non-overlapping intervals.

Check if adjacent intervals overlap.  If they don't overlap, keep the current
interval.  If they overlap, then discard the current interval since it has a 
greater right endpoint.

O(n log n): due to sorting.  Loop is O(n).
O(1) extra space: for in-place sort.
"""
class Solution2:
	def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
		if not a:
			return 0
		
		a.sort(key=lambda x: x[1])
		
		n = len(a)
		count = 1 # count of non-overlapping intervals
		last_endpt = a[0][1]
		
		for i in range(1, n):
			if a[i][0] >= last_endpt: # no overlap
				count += 1
				last_endpt = a[i][1]
				
		return n - count # number of intervals discarded

###############################################################################
"""
Solution 3: DP, sorting by left endpoints.

dp[i] = number of non-overlapping intervals up to interval i

dp[i] = max(dp[j]) + 1 for 0 <= j < i, where intervals i and j don't overlap

O(n^2) time: need a nested loop to check max(dp[j]).
O(n) extra space: for dp table.
"""
class Solution3:
	def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
		if not a:
			return 0

		a.sort()
		n = len(a)
		dp = [1]*n # number of non-overlapping intervals up to interval i

		for i in range(n):
			mx = 0

			for j in range(i):
				if a[i][0] >= a[j][1]: # no overlap
					mx = max(mx, dp[j])

			dp[i] = mx + 1

		return n - max(dp) # number of intervals discarded

###############################################################################
"""
Solution 4: DP, sorting by right endpoints.

dp[i] = number of non-overlapping intervals up to interval i

dp[i] = max(dp[i-1], 1 + max(dp[j])) for 0 <= j < i, 
where intervals i and j don't overlap

There are 2 cases:
(1) Include interval i as a non-overlapping interval.  Need to review prior
intervals j to check which ones don't overlap with interval i.  Take the
max(dp[j]) of these and add 1 for interval i.  Suffices to find the largest
such j by traversing backwards from i-1.

(2) Don't include interval i as a non-overlapping interval.  Then the number
of non-overlapping intervals is just incremented by 1.

O(n^2) time: need a nested loop to check max(dp[j]).
O(n) extra space: for dp table.
"""
class Solution4:
	def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
		if not a:
			return 0

		a.sort(key=lambda x: x[1])
		n = len(a)
		dp = [1]*n # number of non-overlapping intervals up to interval i

		for i in range(n):
			mx = 0

			for j in range(i-1, -1, -1):
				if a[i][0] >= a[j][1]: # no overlap
					mx = max(mx, dp[j])
					break

			dp[i] = max(dp[i-1], 1 + mx)

		return n - max(dp) # number of intervals discarded

###############################################################################

if __name__ == "__main__":
	def test(arr, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\nintervals = {arr}")

		res = sol.eraseOverlapIntervals(arr)

		print(f"\nres = {res}")


	sol = Solution() # greedy, sort by left endpoints
	sol = Solution2() # greedy, sort by right endpoints
	sol = Solution3() # DP, sort by left endpoints
	sol = Solution4() # DP, sort by right endpoints

	comment = "LC ex1; answer = 1"
	arr = [[1,2],[2,3],[3,4],[1,3]]
	test(arr, comment)

	comment = "LC ex2; answer = 2"
	arr = [[1,2],[1,2],[1,2]]
	test(arr, comment)

	comment = "LC ex3; answer = 0"
	arr = [[1,2],[2,3]]
	test(arr, comment)

	comment = "LC test case; answer = 187"
	arr = [
  [
	-100,
	-87
  ],
  [
	-99,
	-44
  ],
  [
	-98,
	-19
  ],
  [
	-97,
	-33
  ],
  [
	-96,
	-60
  ],
  [
	-95,
	-17
  ],
  [
	-94,
	-44
  ],
  [
	-93,
	-9
  ],
  [
	-92,
	-63
  ],
  [
	-91,
	-76
  ],
  [
	-90,
	-44
  ],
  [
	-89,
	-18
  ],
  [
	-88,
	10
  ],
  [
	-87,
	-39
  ],
  [
	-86,
	7
  ],
  [
	-85,
	-76
  ],
  [
	-84,
	-51
  ],
  [
	-83,
	-48
  ],
  [
	-82,
	-36
  ],
  [
	-81,
	-63
  ],
  [
	-80,
	-71
  ],
  [
	-79,
	-4
  ],
  [
	-78,
	-63
  ],
  [
	-77,
	-14
  ],
  [
	-76,
	-10
  ],
  [
	-75,
	-36
  ],
  [
	-74,
	31
  ],
  [
	-73,
	11
  ],
  [
	-72,
	-50
  ],
  [
	-71,
	-30
  ],
  [
	-70,
	33
  ],
  [
	-69,
	-37
  ],
  [
	-68,
	-50
  ],
  [
	-67,
	6
  ],
  [
	-66,
	-50
  ],
  [
	-65,
	-26
  ],
  [
	-64,
	21
  ],
  [
	-63,
	-8
  ],
  [
	-62,
	23
  ],
  [
	-61,
	-34
  ],
  [
	-60,
	13
  ],
  [
	-59,
	19
  ],
  [
	-58,
	41
  ],
  [
	-57,
	-15
  ],
  [
	-56,
	35
  ],
  [
	-55,
	-4
  ],
  [
	-54,
	-20
  ],
  [
	-53,
	44
  ],
  [
	-52,
	48
  ],
  [
	-51,
	12
  ],
  [
	-50,
	-43
  ],
  [
	-49,
	10
  ],
  [
	-48,
	-34
  ],
  [
	-47,
	3
  ],
  [
	-46,
	28
  ],
  [
	-45,
	51
  ],
  [
	-44,
	-14
  ],
  [
	-43,
	59
  ],
  [
	-42,
	-6
  ],
  [
	-41,
	-32
  ],
  [
	-40,
	-12
  ],
  [
	-39,
	33
  ],
  [
	-38,
	17
  ],
  [
	-37,
	-7
  ],
  [
	-36,
	-29
  ],
  [
	-35,
	24
  ],
  [
	-34,
	49
  ],
  [
	-33,
	-19
  ],
  [
	-32,
	2
  ],
  [
	-31,
	8
  ],
  [
	-30,
	74
  ],
  [
	-29,
	58
  ],
  [
	-28,
	13
  ],
  [
	-27,
	-8
  ],
  [
	-26,
	45
  ],
  [
	-25,
	-5
  ],
  [
	-24,
	45
  ],
  [
	-23,
	19
  ],
  [
	-22,
	9
  ],
  [
	-21,
	54
  ],
  [
	-20,
	1
  ],
  [
	-19,
	81
  ],
  [
	-18,
	17
  ],
  [
	-17,
	-10
  ],
  [
	-16,
	7
  ],
  [
	-15,
	86
  ],
  [
	-14,
	-3
  ],
  [
	-13,
	-3
  ],
  [
	-12,
	45
  ],
  [
	-11,
	93
  ],
  [
	-10,
	84
  ],
  [
	-9,
	20
  ],
  [
	-8,
	3
  ],
  [
	-7,
	81
  ],
  [
	-6,
	52
  ],
  [
	-5,
	67
  ],
  [
	-4,
	18
  ],
  [
	-3,
	40
  ],
  [
	-2,
	42
  ],
  [
	-1,
	49
  ],
  [
	0,
	7
  ],
  [
	1,
	104
  ],
  [
	2,
	79
  ],
  [
	3,
	37
  ],
  [
	4,
	47
  ],
  [
	5,
	69
  ],
  [
	6,
	89
  ],
  [
	7,
	110
  ],
  [
	8,
	108
  ],
  [
	9,
	19
  ],
  [
	10,
	25
  ],
  [
	11,
	48
  ],
  [
	12,
	63
  ],
  [
	13,
	94
  ],
  [
	14,
	55
  ],
  [
	15,
	119
  ],
  [
	16,
	64
  ],
  [
	17,
	122
  ],
  [
	18,
	92
  ],
  [
	19,
	37
  ],
  [
	20,
	86
  ],
  [
	21,
	84
  ],
  [
	22,
	122
  ],
  [
	23,
	37
  ],
  [
	24,
	125
  ],
  [
	25,
	99
  ],
  [
	26,
	45
  ],
  [
	27,
	63
  ],
  [
	28,
	40
  ],
  [
	29,
	97
  ],
  [
	30,
	78
  ],
  [
	31,
	102
  ],
  [
	32,
	120
  ],
  [
	33,
	91
  ],
  [
	34,
	107
  ],
  [
	35,
	62
  ],
  [
	36,
	137
  ],
  [
	37,
	55
  ],
  [
	38,
	115
  ],
  [
	39,
	46
  ],
  [
	40,
	136
  ],
  [
	41,
	78
  ],
  [
	42,
	86
  ],
  [
	43,
	106
  ],
  [
	44,
	66
  ],
  [
	45,
	141
  ],
  [
	46,
	92
  ],
  [
	47,
	132
  ],
  [
	48,
	89
  ],
  [
	49,
	61
  ],
  [
	50,
	128
  ],
  [
	51,
	155
  ],
  [
	52,
	153
  ],
  [
	53,
	78
  ],
  [
	54,
	114
  ],
  [
	55,
	84
  ],
  [
	56,
	151
  ],
  [
	57,
	123
  ],
  [
	58,
	69
  ],
  [
	59,
	91
  ],
  [
	60,
	89
  ],
  [
	61,
	73
  ],
  [
	62,
	81
  ],
  [
	63,
	139
  ],
  [
	64,
	108
  ],
  [
	65,
	165
  ],
  [
	66,
	92
  ],
  [
	67,
	117
  ],
  [
	68,
	140
  ],
  [
	69,
	109
  ],
  [
	70,
	102
  ],
  [
	71,
	171
  ],
  [
	72,
	141
  ],
  [
	73,
	117
  ],
  [
	74,
	124
  ],
  [
	75,
	171
  ],
  [
	76,
	132
  ],
  [
	77,
	142
  ],
  [
	78,
	107
  ],
  [
	79,
	132
  ],
  [
	80,
	171
  ],
  [
	81,
	104
  ],
  [
	82,
	160
  ],
  [
	83,
	128
  ],
  [
	84,
	137
  ],
  [
	85,
	176
  ],
  [
	86,
	188
  ],
  [
	87,
	178
  ],
  [
	88,
	117
  ],
  [
	89,
	115
  ],
  [
	90,
	140
  ],
  [
	91,
	165
  ],
  [
	92,
	133
  ],
  [
	93,
	114
  ],
  [
	94,
	125
  ],
  [
	95,
	135
  ],
  [
	96,
	144
  ],
  [
	97,
	114
  ],
  [
	98,
	183
  ],
  [
	99,
	157
  ]
]
	test(arr, comment)
