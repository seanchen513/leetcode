"""
23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]

Output: 1->1->2->3->4->4->5->6
"""
from typing import List
from linked_list import ListNode, build_ll
import heapq

"""
class ListNode():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

    # Needed for sorted merge of k sorted linked lists.
    def __lt__(self, other):
        return self.val < other.val
"""

###############################################################################
""" OPTIMAL SOLUTION
Solution 1: Use min heap to store heads of each list.
Assume function __lt__() has been defined in class ListNode.

Note: heappop() and heappush() are O(log k), where k is the number of lists.

O(n log k) time, where n is total number of elements among all input lists.
O(mk log k) time if all atomic lists have approx. length m.

O(k) extra space for heap
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []
        for ll in lists:
            if ll:
                heapq.heappush(heads, ll)

        header = ListNode() # dummy header node
        tail = header

        while heads:
            m = heapq.heappop(heads) # temp var for readibility
            tail.next = m
            tail = tail.next

            if m.next:
                heapq.heappush(heads, m.next)
        
        return header.next # could return header.next, tail

###############################################################################
"""
Solution 1b:
Same as solution 1 using min heap, 
BUT don't assume function __lt__() has been defined in class ListNode.
Instead, store tuples (node value, index in lists) in heap rather than nodes.
"""
class Solution1b:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heads, (lists[i].val, lists[i]))
        
        header = ListNode() # dummy header node
        tail = header

        while heads:
            _, node = heapq.heappop(heads)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heads, (node.next.val, node.next))

        return header.next # could return header.next, tail

###############################################################################
"""
Solution 2: 
Use array to store heads of each list.
Assume __lt__() is defined in class ListNode, but don't have to if
store tuples (node value, index of lists, node) in array.

Can either: 
(1) sort array vals and extract the min node each time, or
(2) find min node each time.

O(nk + k log k) time, where n = total number of elements among all input lists.
O(k) extra space for array that stores heads of lists.
O(1) extra space if reuse given lists.
"""
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = [ll for ll in lists if ll]
                
        header = ListNode() # dummy node
        tail = header

        while heads:
            # After first iteration, should be O(k) since we only appended one
            # item to sorted list.  First iteration is O(k log k).
            # Sort in reverse to make it easy to remove the min node.
            heads = sorted(heads, reverse=True)
            
            tail.next = heads.pop()
            tail = tail.next
            if tail.next:
                heads.append(tail.next)

        return header.next # could return header.next, tail

##############################################################################
"""
Solution 3: repeatedly merge 2 sorted linked lists at a time.

O(m * k^2) = O(nk) time if all k sorted lists have approx. length m.
O(1) extra space

Assume each sorted list has length m.
Merging sorted lists of lengths a and b is O(a+b).
The first merge is for None with the first list, so is O(1).

2m + 3m + ... + km = m(2 + 3 + ... + k) = m[k(k+1)/2 - 1] = O(m * k^2)
"""
class Solution3:
    def merge_two_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode() # dummy header for merged list
        node = header

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next

            node = node.next

        if l1: node.next = l1
        elif l2: node.next = l2

        return header.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        from functools import reduce
        return reduce(self.merge_two_sorted_lists, lists) if lists else None

###############################################################################
"""
Solution 4: divide & conquer, merging 2 sorted lists at at time.

O(n log k) time
O(1) extra space

First pass has n/2 merges of two 1-element lists.
Second pass has n/4 merges of two lists with 2 elements each
Last pass has 2 merges of two lists with n/2 elements each.
Each pass, the merges have total O(n) time.
There are log_2(k) passes, so overall time is O(n log k)
"""
class Solution4:
    def merge_two_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode() # dummy header for merged list
        node = header

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next

            node = node.next

        if l1: node.next = l1
        elif l2: node.next = l2

        return header.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n - interval, 2 * interval):
                lists[i] = self.merge_two_sorted_lists(lists[i], lists[i+interval])

            interval *= 2

        return lists[0] if n > 0 else None

###############################################################################

if __name__ == "__main__":
    def test(arrays, comment=None):
        lists = []
        for arr in arrays:
            lists += [build_ll(arr)[0]]
        
        print("="*80)
        if comment:
            print(comment)

        # lists are modified after the merge
        print("\nOriginal sorted lists:") 
        for ll in lists:
            print(ll)
        
        head = s.mergeKLists(lists)

        print("\nSorted, merged linked list:")
        print(head)
        print()

        #print("\nVerify that it is actually sorted:")

    def test_self_merge(arr):
        lst = build_ll(arr)[0]
        _ = s.mergeKLists([lst, lst]) # infinite loop


    #s = Solution() # min heap w/ __lt__() defined in ListNode
    s = Solution1b() # min heap storing (node.val, index, node)
    #s = Solution2() # use list to store heads, and repeatedly sort
    #s = Solution3() # merge 2 lists at a time
    #s = Solution4() # divide & comquer, merging 2 lists at a time

    comment = "=== LC example"
    arrays = [[1,4,5], [1,3,4], [2,6]]
    test(arrays, comment)

    #comment = "=== Lists of unequal length"
    #arrays = [[1, 2, 3, 17], [-5, 6, 13], [7, 8], [4]]
    #test(arrays, comment)

    ### Edge cases
    # test([], "Empty list of lists")
    # test([None], "One list that is None")
    # test([None, None, None], "Three lists that are each None")
    # test([[1,2,3]], "Nonempty list by itself")
    # test([[1,2,3], None], "Nonempty list with list None")
    # test([None, [1,2,3], None], "Nonempty list with None lists before and after")
    # test([[7],[0],[-5],[3]], "Lists of single elements")

    #test_self_merge([1,2,3,4,5]) # this will hang; infinite loop

    # import random
    # comment = "=== Lists of randomly generated ints"
    # arrays = [
    #     sorted([random.randint(1, 100) for _ in range(5)]),
    #     sorted([random.randint(1, 100) for _ in range(3)]),
    #     sorted([random.randint(1, 100) for _ in range(4)]),
    # ]
    # test(arrays, comment)
