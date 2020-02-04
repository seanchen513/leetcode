"""
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

###############################################################################
"""
Solution 1: brute force

LC TLE
"""
class Solution:    
    # assume n > 0
    def is_ugly(self, n: int) -> bool:
        while n % 5 == 0:
            n //= 5

        while n % 3 == 0:
            n //= 3
        
        while n & 1 == 0:
            n >>= 1
            
        return n == 1

    def nthUglyNumber(self, n: int) -> int:
        i = 0

        while n > 0:
            i += 1
            if self.is_ugly(i):
                n -= 1

        return i

###############################################################################
"""
Solution 2: Keep uglies array and 3 indices to track the next ugly number
waiting to be multiplied by 2, 3, or 5.

Every ugly numbers comes from multiplying a smaller (previous) ugly number
by 2, 3, or 5.  Each ugly number generates 3 bigger ugly numbers.

This is like merging 3 sorted linked lists.

O(n) time
O(n) extra space
"""
class Solution2:    
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        i = j = k = 0 # indices in "uglies" array

        while n > 1:
            a, b, c = 2*uglies[i], 3*uglies[j], 5*uglies[k]
            ugly = min(a, b, c)
            uglies += [ugly] # looping over list appends is expensive

            if ugly == a: i += 1
            if ugly == b: j += 1
            if ugly == c: k += 1

            n -= 1

        return uglies[-1]

"""
Solution 2b: same as solution 2, but rewritten.
"""
class Solution2b:    
    def nthUglyNumber(self, n: int) -> int:
        uglies = [0]*n
        uglies[0] = 1
        p1 = p2 = p3 = 0 # indices/"pointers" in "uglies" array

        for i in range(1, n):
            a, b, c = 2*uglies[p1], 3*uglies[p2], 5*uglies[p3]
            uglies[i] = ugly = min(a, b, c)
            
            if ugly == a: p1 += 1
            if ugly == b: p2 += 1
            if ugly == c: p3 += 1

        return uglies[-1]

###############################################################################
"""
Solution 3: use heap, but have to deal with duplicates by popping them all
when encountered.
"""
from heapq import heappush, heappop

class Solution3:    
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]

        for _ in range(1, n):
            ugly = heappop(heap)
            while heap and heap[0] == ugly:
                heappop(heap)

            heappush(heap, ugly*2)
            heappush(heap, ugly*3)
            heappush(heap, ugly*5)

        return heap[0]

"""
Solution 3b: use heap.  Deal with duplicates by checking vs a set
before adding to the heap.

Better to use a heap that is also a set...

O(n log n) time - loop n times; heap insert/remove are O(log n)
O(n) extra space

[set operations are O(1) amortized avg case, but O(n) actual worst case...]
"""
class Solution3b:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        pushed = set([1])

        for _ in range(1, n):
            ugly = heappop(heap) # O(log n)
            
            for p in (2, 3, 5):
                new_ugly = ugly * p
                if new_ugly not in pushed: # O(1) amortized avg, O(n) worst
                    heappush(heap, new_ugly) # O(log n)
                    pushed.add(new_ugly) # O(1) amortized avg, O(n) worst

        return heap[0]

###############################################################################
"""
Solution 4: use 3 queues.  Each queue holds the next element to be used
that just multiplied by 2, 3, or 5.

This is faster than using heaps, but a little slower than just keeping 
an array and 3 pointers.
"""
from collections import deque

class Solution4:
    def nthUglyNumber(self, n: int) -> int:
        q1 = deque([1])
        q2 = deque([1])
        q3 = deque([1])

        for _ in range(0, n):
            ugly = min(q1[0], q2[0], q3[0])
            if ugly == q1[0]: q1.popleft()
            if ugly == q2[0]: q2.popleft()
            if ugly == q3[0]: q3.popleft()

            q1.append(2*ugly)
            q2.append(3*ugly)
            q3.append(5*ugly)

        return ugly

###############################################################################

if __name__ == "__main__":
    def test_ints(ints):
        #s = Solution()
        #s = Solution2()
        s = Solution2b()
        #s = Solution3()
        #s = Solution3b()
        #s = Solution4()

        res = {}
        for n in ints:
            res[n] = s.nthUglyNumber(n)

        print()
        print(res)

    def test(arr):
        solutions = [Solution(), Solution2(), Solution2b(), 
            Solution3(), Solution3b(), Solution4()]

        for n in arr:
            res = []
            for s in solutions:
                res += [s.nthUglyNumber(n)]

            print("="*80)
            print(f"Testing results of solutions for n = {n}\n")
            print(res)

    def test_times(n=100):
        from timeit import default_timer as timer

        solutions = [
            #Solution(), # brute force 
            Solution2(), # 3 ptrs w/ looped list appends
            Solution2b(), # 3 ptrs w/ premade array
            Solution3(), # heap
            Solution3b(), # heap, w/ set to deal with duplicates
            Solution4(), # use 3 queues
            ]

        times = []

        for s in solutions:
            start = timer()
            s.nthUglyNumber(n)
            t = timer() - start
            times += [t]

        print("="*80)
        print(f"\nTesting times for solutions with n = {n}\n")
        for i in range(len(times)):
            print(times[i])


    #ints = list(range(1, 100))
    #test_ints(ints)

    arr = [1, 12, 200]
    test(arr)

    #test_times(500) # if include brute force solution
    #test_times(50000)
