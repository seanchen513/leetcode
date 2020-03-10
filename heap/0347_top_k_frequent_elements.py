"""
47. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List
import collections
import heapq

###############################################################################
"""
Solution: use dict to count frequency of each element.  Then push all
tuples (count, x) into min heap of size k.

O(n log k) time: for at most n heap operations on heap of size at most k.
O(n log n) time if k ~ n.

O(n) extra space: for dict to count elements.
"""
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        
        for x in arr:
            d[x] += 1
            
        h = [] # min heap
        
        for x, count in d.items():
            if len(h) == k:
                heapq.heappushpop(h, (count,x))
            else:
                heapq.heappush(h, (count, x))
            
        return [x for _, x in h]

"""
Solution 1b: same as sol 1, but push all tuples (-count, x) into max heap, then
pop k elements.

O(n + k log n) time: for heapify, and for popping k elements from heap of
size at most n.
O(n log n) if k ~ n.

O(n) extra space: for dict to count elements.
"""
class Solution1b:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        
        for x in arr:
            d[x] += 1
            
        h = [(-count, x) for x, count in d.items()] # max heap

        heapq.heapify(h) # O(n)
            
        res = []

        for _ in range(k): # O(k log n)
            res.append(heapq.heappop(h)[1])

        return res

###############################################################################
"""
Solution 2: use heapq.nlargest().

O(n log k) time?
"""
class Solution2:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d = collections.Counter(arr)
        return heapq.nlargest(k, d.keys(), key=d.get)

"""
Solution 2b: use Counter.most_common(), which uses heapq.nlargest() under
the hood.

O(n log k) time?
"""
class Solution2b:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        k_most_common = collections.Counter(arr).most_common(k)
        return [x for x, _ in k_most_common]

###############################################################################
"""
Solution 3: bucket sort.  No heap, no sorting, no Counter().

O(n) time?

O(n) extra space

### If all elements distinct:
d[x] = 1 for all x
len(d) = n

freq[1] = [...] same as arr

res.extend(freq[times]) non-trival only for times = 1

### If all elements equal x:
d[x] = n
len(d) = 1

freq[n] = [x]

res.extend(freq[times]) non-trival only for times = n

"""
class Solution3:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        # count = collections.Counter(arr)
        count = collections.defaultdict(int)
        for x in arr:
            count[x] += 1
        
        freq = collections.defaultdict(list) # buckets for counts
        for x, cnt in count.items():
            freq[cnt].append(x)

        max_count = max(freq.keys())
        res = []

        # At most a total of k elts added to "res".
        # O(n) excluding extend() and return.
        # Total work done by extend() is O(n) total for all the empty lists
        # and O(k) total for all the non-empty lists.
        # Array copy "res[:k]" is O(k).
        # Overall O(n).
        
        #for times in range(len(arr), 0, -1):
        for times in range(max_count, 0, -1):
            # res.extend( freq[times] ) 
            # if len(res) >= k:
            #     return res[:k]

            for x in freq[times]:
                res.append(x)
                if len(res) == k:
                    return res

        return res

###############################################################################
"""
Solution 4: use quickselect w/ random pivots.

O(n) time avg, O(n^2) worst case
O(n) time worst case if added median-of-medians method to feed initial
pivots into partition().  This also adds O(log n) extra space.

O(n) extra space for "count" dict.

"""
import random
class Solution4:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        def partition(a, start, end):
            pv = a[end] # pivot value
            i = start # next pos to swap smaller-than-pivot elt to

            # Move all elements smaller than pivot to left of pivot.
            for j in range(start, end):
                if a[j] < pv:
                    a[i], a[j] = a[j], a[i]
                    i += 1

            # Now, "i" is index of first elt >= pivot, ie, the first duplicate 
            # of pivot, or the first elt larger than the pivot.

            # Move pivot to its proper position.
            a[i], a[end] = a[end], a[i]

            return i # pivot value is now at index i

        count = collections.defaultdict(int)
        for x in arr:
            count[x] += 1

        a = [(-cnt, x) for x, cnt in count.items()] # -cnt so we get largest k elts

        start, end = 0, len(a)-1
        k -= 1 # given k is 1-based, but our algo is 0-based

        while start <= end:
            if start == end: # this part isn't necessary... both == k
                a_k = a[:k+1]
                return [x for _, x in a_k]

            # Pick random initial pivot to feed into partition(), and swap to "end".
            p = random.randint(start, end) # inclusive
            a[p], a[end] = a[end], a[p]

            p = partition(a, start, end) # pivot index

            if p == k:
                a_k = a[:k+1]
                return [x for _, x in a_k]
            elif p > k: # then we can ignore elts from p on since they are too big
                end = p - 1
            else: # p < k; we still need to find small elts to put b/w p and k
                start = p + 1

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)
        print(f"k = {k}")

        res = sol.topKFrequent(arr, k)

        print(f"\nres = {res}\n")


    sol = Solution() # use min heap of size k
    sol = Solution1b() # use max heap
    
    sol = Solution2() # use heapq.nlargest()
    sol = Solution2b() # use Counter.most_common(k)
    
    sol = Solution3() # bucket sort; no heap, no sorting, no Counter()
    sol = Solution4() # quickselect

    comment = "LC ex1; answer = [1,2]"
    arr = [1,1,1,2,2,3]
    k = 2
    test(arr, k, comment)

    comment = "LC ex2; answer = [1]"
    arr = [1]
    k = 1
    test(arr, k, comment)

    comment = "LC test case; answer = [1,2]"
    arr = [1,2]
    k = 2
    test(arr, k, comment)

    comment = "LC test case; answer = [1,3]"
    arr = [5,3,1,1,1,3,73,1]
    k = 2
    test(arr, k, comment)

