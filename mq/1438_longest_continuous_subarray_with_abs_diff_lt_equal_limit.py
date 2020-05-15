"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 

Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""

from typing import List
import collections
import bisect
import heapq

###############################################################################
"""
Solution: use sliding window with inc queue for min and dec queue for max.
Maintain loop invariant: sliding window satisfies problem condition.

Two pointers: left and right ends of sliding window (subarray).

Start with left pointer l and right pointer r at index 0. 
Iterate over right pointer r.
Maintain min/max queues, then append r to both.
If max - min > limit, then popleft() 0th elt of queues if their array value
equals arr[l]. Increment l.

This gives the longest subarray ending at r and that satisfies condition.
Track max length = r - l + 1.

Max abs diff b/w any 2 elts within window = max within window - min within window.

Tricky part is how to efficiently get the max and min within the window.
Two monotone queues to track min and max within sliding window.
- min queue is increasing; min[0] is min within window
- max queue is decreasing; max[0] is max within window

O(n) time: each element enters/leaves each deque at most once
O(n) extra space

https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609708/Python-Clean-Monotonic-Queue-solution-with-detail-explanation-O(N)

Runtime: 372 ms, faster than 97.37% of Python3 online submissions
Memory Usage: 24 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        l = 0 # index of left end of sliding window (subarray)
        res = 0

        min_deque = collections.deque() # inc queue
        max_deque = collections.deque() # dec queue

        for r, x in enumerate(arr): # r = index of right end of sliding window (subarray)
            # Maintain increasing queue.
            while min_deque and x < arr[min_deque[-1]]: # can use < or <=
                min_deque.pop()

            # Maintain decreasing queue.
            while max_deque and x > arr[max_deque[-1]]: # can use > or >=
                max_deque.pop()

            min_deque.append(r)
            max_deque.append(r)

            # Maintain loop invariant: sliding window satisfies problem condition.
            while arr[max_deque[0]] - arr[min_deque[0]] > limit:
                # l += 1
                # if l > min_deque[0]:
                #     min_deque.popleft()
                # if l > max_deque[0]:
                #     max_deque.popleft()

                if l == min_deque[0]:
                    min_deque.popleft()

                if l == max_deque[0]:
                    max_deque.popleft()

                l += 1

            if r - l > res:
                res = r - l

        return res + 1

"""
Solution 1b: same, but let sliding window grow monotonically.
"""
class Solution1b:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        l = 0 # index of left end of sliding window (subarray)

        min_deque = collections.deque() # inc queue
        max_deque = collections.deque() # dec queue

        for r, x in enumerate(arr): # r = index of right end of sliding window (subarray)
            # Maintain increasing queue.
            while min_deque and x < arr[min_deque[-1]]: # can use < or <=
                min_deque.pop()

            # Maintain decreasing queue.
            while max_deque and x > arr[max_deque[-1]]: # can use > or >=
                max_deque.pop()

            min_deque.append(r)
            max_deque.append(r)

            if arr[max_deque[0]] - arr[min_deque[0]] > limit:                
                # Increment l (left end of window) and update queues.
               
                # l += 1
                # if l > min_deque[0]:
                #     min_deque.popleft()
                # if l > max_deque[0]:
                #     max_deque.popleft()

                if l == min_deque[0]:
                    min_deque.popleft()

                if l == max_deque[0]:
                    max_deque.popleft()

                l += 1

        return len(arr) - l

###############################################################################
"""
Solution 2: same, but store values instead of indices.
Maintain loop invariant: sliding window satisfies problem condition.

https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

Runtime: 340 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 24 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        l = 0 # index of left end of sliding window (subarray)
        res = 0

        min_deque = collections.deque() # inc queue
        max_deque = collections.deque() # dec queue

        for r, x in enumerate(arr):
            # Maintain increasing queue.
            while min_deque and x < min_deque[-1]: # <= does not work
                min_deque.pop()

            # Maintain decreasing queue.
            while max_deque and x > max_deque[-1]: # >= does not work
                max_deque.pop()

            min_deque.append(x)
            max_deque.append(x)

            # Increment l (left end of window) and update queues.
            while max_deque[0] - min_deque[0] > limit:
                if min_deque[0] == arr[l]:
                    min_deque.popleft()

                if max_deque[0] == arr[l]:
                    max_deque.popleft()

                l += 1

            if r - l > res:
                res = r - l

        return res + 1

"""
Solution 2b: same, but let sliding window grow monotonically.
"""
class Solution2b:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        l = 0 # index of left end of sliding window (subarray)

        min_deque = collections.deque() # inc queue
        max_deque = collections.deque() # dec queue

        for x in arr:
            # Maintain increasing queue.
            while min_deque and x < min_deque[-1]: # <= does not work
                min_deque.pop()

            # Maintain decreasing queue.
            while max_deque and x > max_deque[-1]: # >= does not work
                max_deque.pop()

            min_deque.append(x)
            max_deque.append(x)

            # Increment l (left end of window) and update queues.
            # Using "while" loop does not work.
            if max_deque[0] - min_deque[0] > limit:
                if min_deque[0] == arr[l]:
                    min_deque.popleft()

                if max_deque[0] == arr[l]:
                    max_deque.popleft()

                l += 1

            #if l < 10 and len(min_deque) < 10:
            # if len(arr) < 20:
            #     print("\nAFTER:")
            #     print(f"l = {l}")
            #     print(f"min_deque = {list(min_deque)}")
            #     print(f"max_deque = {list(max_deque)}")
            #     if len(arr) - l < 20:
            #         print(f"(NOT necc window) arr[l:] = {arr[l:]}")

        return len(arr) - l

"""
LC ex2:
[10,1,2,4,7,2]
limit = 5

l = 0, arr[l] = 10

x = 10
mind = [10]
maxd = [10]
max - min = 10 - 10 = 0 <= limit = 5
window = [10]

x = 1
mind.pop(): 10
mind = [1]
maxd = [10, 1]
max - min = 10 - 1 = 9 > limit = 5
arr[l] = arr[0] = 10
    maxd.pop(): 10
    maxd = [1]
    l += 1, so l = 1 now
window = [1]

l = 1, arr[l] = 1

x = 2
maxd.pop(): 10
mind = [1,2]
maxd = [2]
max - min = 2 - 1 = 1 <= limit = 5
window = [1,2]

x = 4
maxd.pop(): 2
mind = [1,2,4]
maxd = [4]
max - min = 4 - 1 = 3 <= limit = 5
window = [1,2,4]

x = 7
maxd.pop(): 4
mind = [1,2,4,7]
maxd = [7]
max - min = 7 - 1 = 6 > limit = 5
arr[l] = arr[1] = 1
    mind.pop(): 1
    mind = [2,4,7]
    l += 1, so l = 2 now
window = [2,4,7]

l = 2, arr[l] = 2

x = 2
mind.pop(): 7, 4
mind = [2,2]
maxd = [7,2]
max - min = 7 - 2 = 5 <= limit = 5
window = [2,4,7,2]

"""

###############################################################################
"""
Solution 3: sliding window with sorted list and binary insert/remove.

Keep sorted list of values from current sliding window.
Loop invariant: sorted list (and window) satisfies problem condition:
abs diff of any two elts <= limit.

This makes it easy to access the min and max elements in the window.
Insert new elements in sorted order.
If range of sorted list exceeds limit, binary search for the elt leftmost 
in array and remove it from sorted list.

This is slow because of a lot of unnecessary pops in inner "while" loop
to maintain loop invariant.

O(n^2) time: due to list.pop() within loop
O(n) extra space: for sorted list

Runtime: 1580 ms, faster than 5.78% of Python3 online submissions
Memory Usage: 23.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        res = 0

        l = 0 # left end of sliding window (subarray)
        s = [] # sorted list
        
        for r in range(n):
            bisect.insort(s, arr[r])

            # Remove elements from left side until sliding window satisfies
            # problem condition.
            # Solution happens to work if "while" is replaced by "if", but...
            while s[-1] - s[0] > limit:
                # Note: we are removing the element in s that is leftmost
                # in the input array. This is usually not the same as the
                # smallest/first element in s.
                s.pop( bisect.bisect_left(s, arr[l]) )
                l += 1
            
            if r - l > res:
                res = r - l

        return res + 1

"""
Solution 3b: same, but instead of forcing sorted list (sliding window) to
satisfy problem condition at all times, only pop elements one at a time
when necessary.

The sorted list grows monotonically. It never shrinks when moving from one 
index to the next. In each iteration, a new element is added, and either no 
element is removed or one element is removed. Once the sorted list reaches 
max size, it stays there.

Note: doesn't work if we change the inner "if" statement into a 
"while" loop.

Runtime: 348 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 23.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution3b:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)

        l = 0 # left end of sliding window (subarray)
        s = [] # sorted list

        for r in range(n):
            bisect.insort(s, arr[r])

            if s[-1] - s[0] > limit: # cannot use "while" loop here
                # Note: we are removing the element in s that is leftmost
                # in the input array. This is usually not the same as the
                # smallest/first element in s.
                s.pop( bisect.bisect_left(s, arr[l]) )
                l += 1

        #return r - l + 1
        #return n - l # after loop, r = n-1
        return len(s)

"""
LC ex2:
[10,1,2,4,7,2]
limit = 5

l = 0
r=0, x=10
insort([], 10)
s = [10]
s[-1] - s[0] = 10 - 10 = 0 <= limit = 5

r=1, x=1
insort([10], 1)
s = [1, 10]
s[-1] - s[0] = 10 - 1 = 9 > limit = 5
    s.pop( bisect_left([1,10], arr[l]=arr[0]=1)) # remove leftmost elt in window
    ie, s.pop(10)
    s = [1]
    l += 1, so l now 1

l = 1

r=2, x=2
insort([1], 2)
s = [1, 2]
s[-1] - s[0] = 2 - 1 = 1 <= limit = 5

r=3, x=4
insort([1,2], 4)
s = [1, 2, 4]
s[-1] - s[0] = 4 - 1 = 3 <= limit = 5

r=4, x=7
insort([1,2,4], 7)
s = [1, 2, 4, 7]
s[-1] - s[0] = 7 - 1 = 6 > limit = 5
    s.pop( bisect_left([1,2,4,7], arr[l]=arr[1]=1)) # remove leftmost elt in window
    ie, s.pop(1)
    s = [2,4,7]
    l += 1, so l now 2

l = 2

r=5, x=2
insort([2,4,7], 2)
s = [2, 2, 4, 7]
s[-1] - s[0] = 7 - 2 = 5 <= limit = 5

return r - l + 1 = 5 - 2 + 1 = 4

"""

###############################################################################
"""
Solution 4: use sortedcontainer's SortedDict. 

Loop invariant: force sliding window to maintain problem condition.

Similar to using sorted list, but avoids list pop()'s O(n) time.
Instead, del d[] and d update are O(1). (Note: d.pop() is O(log n).)
On the other hand, looking up max and min takes O(log n) instead of O(1) time.

Java: TreeMap
C++: multiset (multi treeset, even better than tree map?)

O(n log n) time: since peekitem() is O(log n)
O(n) extra space

Runtime: 824 ms, faster than 29.22% of Python3 online submissions
Memory Usage: 24.3 MB, less than 100.00% of Python3 online submissions

Note: early break/return if n - l <= res doesn't make it faster.
"""
import sortedcontainers
class Solution4:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        d = sortedcontainers.SortedDict()
        l = 0 # left index of sliding window
        res = 0

        for r, x in enumerate(arr):
            #d[x] = d.get(x, 0) + 1
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            
            # Happens to work with "if", but...
            while d.peekitem()[0] - d.peekitem(0)[0] > limit:
                if d[arr[l]] == 1:
                    #d.pop(arr[l]) # O(log n)
                    del d[arr[l]] # faster since O(1)
                else:
                    d[arr[l]] -= 1

                l += 1
            
            if r - l > res:
                res = r - l

        return res + 1

"""
Solution 4b: same, but instead of forcing sliding window to satisfy problem
condition, let it grow monotonically...

"""
import sortedcontainers
class Solution4b:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        d = sortedcontainers.SortedDict()
        l = 0 # left index of sliding window

        for x in arr:
            #d[x] = d.get(x, 0) + 1
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            
            if d.peekitem()[0] - d.peekitem(0)[0] > limit:
                if d[arr[l]] == 1:
                    #d.pop(arr[l]) # O(log n)
                    del d[arr[l]] # faster since O(1)
                else:
                    d[arr[l]] -= 1

                l += 1
            
        return len(arr) - l
        #return sum(d.values())

###############################################################################
"""
Solution 5: use two heaps of (val, index).

mins: min heap
maxes: max heap

Max abs diff within sliding window can be calculated from tops of heaps easily.
While this is > limit, update left end of window to exclude the leftmost
extremum and all points before it, and remove all elements from both heaps that
are outside the updated window.

O(n log n) time
O(n) extra space

Runtime: 532 ms, faster than 60.00% of Python3 online submissions
Memory Usage: 35.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution5:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        l = 0 # left end of sliding window (subarray)
        res = 0
        minq = []
        maxq = []

        for r, x in enumerate(arr):
            heapq.heappush(minq, [x, r])
            heapq.heappush(maxq, [-x, r])

            # while max abs diff within sliding window is > limit
            while -maxq[0][0] - minq[0][0] > limit:
                # Update left end of sliding window to exclude the leftmost
                # extremum and all elements before it.
                l = min(maxq[0][1], minq[0][1]) + 1
                
                # Remove all elements from both heaps that are outside the
                # updated window.

                while maxq[0][1] < l:
                    heapq.heappop(maxq)

                while minq[0][1] < l:
                    heapq.heappop(minq)

            res = max(res, r - l)

        return res + 1

###############################################################################
"""
Solution 6: brute force w/ early break/return if n - i < res.

TLE's w/o early break.

O() time ???
O(1) extra space

Runtime: 612 ms, faster than 40.00% of Python3 online submissions
Memory Usage: 23.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution6:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        res = 1 # max length

        for i in range(n):
            if n - i < res:
                break

            mn = mx = arr[i]

            for j in range(i+1, n):
                x = arr[j]
                if x < mx - limit or x > mn + limit:
                    break

                mn = min(mn, x)
                mx = max(mx, x)
                res = max(res, j - i + 1)

        return res

"""
Solution 6b: same, but using for-else.

Runtime: 512 ms, faster than 81.70% of Python3 online submissions
Memory Usage: 23.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution6b:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        res = 1 # max length

        for i in range(n):
            if n - i < res:
                break

            mn = mx = arr[i]

            for j in range(i+1, n):
                x = arr[j]
                if x < mx - limit or x > mn + limit:
                    res = max(res, j - i)
                    break

                mn = min(mn, x)
                mx = max(mx, x)
            else:
                res = max(res, n - i)

        return res

"""
Solution 6c: same, but optimized a bit (no for-else).

Runtime: 404 ms, faster than 80.00% of Python3 online submissions
Memory Usage: 24 MB, less than 100.00% of Python3 online submissions
"""
class Solution6c:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        res = 0

        for i in range(n):
            if n - i < res:
                break

            mx = mn = arr[i]
            mx_limit = mx - limit
            mn_limit = mn + limit
            
            for j in range(i+1, n):
                x = arr[j]
                if x < mx_limit or x > mn_limit:
                    break

                if x < mn:
                    mn = x
                    mn_limit = mn + limit
                if x > mx:
                    mx = x
                    mx_limit = mx - limit
                if j - i > res:
                    res = j - i

        return res + 1

"""
Solution 6d: same, but optimized a bit and using for-else.

Runtime: 372 ms, faster than 97.37% of Python3 online submissions
Memory Usage: 23.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution6d:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        res = 1

        for i in range(n):
            if n - i < res:
                break

            mx = mn = arr[i]
            mx_limit = mx - limit
            mn_limit = mn + limit
            
            for j in range(i+1, n):
                x = arr[j]
                if x < mx_limit or x > mn_limit:
                    if j - i > res:
                        res = j - i
                    break

                if x < mn:
                    mn = x
                    mn_limit = mn + limit
                if x > mx:
                    mx = x
                    mx_limit = mx - limit
            
            else:
                if n - i > res:
                    res = n - i

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, limit, comment=None):
        print("="*80)
        if comment:
            print(comment)

        if len(arr) < 20:
            print(f"\narr = {arr}")
        else:
            print(f"\narr[:20] = {arr[:20]}")

        print(f"len(arr) = {len(arr)}")
        print(f"limit = {limit}")

        res = sol.longestSubarray(arr, limit)

        print(f"\nres = {res}\n")


    sol = Solution() # use sliding window with inc queue for min and dec queue for max
    sol = Solution1b() # same, but let swindow grow monotonically

    sol = Solution2() # same as sol 1, but store values instead of indices
    sol = Solution2b() # same, but let swindow grow monotonically

    #sol = Solution3() # sliding window with sorted list and binary insert/remove.
    sol = Solution3b() # same, but let swindow grow monotonically
    #sol = Solution4() # use sortedcontainer's SortedDict instead of sorted list
    sol = Solution4b() # same, but let swindow grow monotonically
    
    #sol = Solution5() # two heaps

    #sol = Solution6() # brute force
    #sol = Solution6b() # same, but using for-else
    #sol = Solution6c() # optimized a bit
    #sol = Solution6d() # optimized a bit, using for-else

    comment = "LC ex1; answer = 2"
    arr = [8,2,4,7]
    limit = 4
    test(arr, limit, comment)

    comment = "LC ex2; answer = 4"
    arr = [10,1,2,4,7,2]
    limit = 5
    test(arr, limit, comment)

    comment = "LC ex3; answer = 3"
    arr = [4,2,2,2,4,4,2,2]
    limit = 0
    test(arr, limit, comment)

    comment = "LC TC; answer = 9"
    arr = [7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
    limit = 63    
    test(arr, limit, comment)

    comment = "LC TC; answer = 100000"
    arr = [1] * 100000
    limit = 10
    test(arr, limit, comment)

    import random
    comment = "Randomly generated array"
    arr = [random.randint(1,100) for _ in range(1000)]
    limit = 80
    test(arr, limit, comment)
