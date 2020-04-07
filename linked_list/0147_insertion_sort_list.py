"""
147. Insertion Sort List
Medium

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################################################################
"""
Solution: convert linked list to array of ListNode's, sort array by node
values, then relink nodes in array.

O(n log n) time: for sorting array of list nodes
O(n) extra space: for array
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        arr = []

        while head:
            arr.append(head)
            head = head.next

        arr.sort(key=lambda node: node.val)

        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]

        arr[-1].next = None
            
        return arr[0]

###############################################################################
"""
Solution 2: insertion sort for linked list.

pre -> pre.next
    pre.val < curr.val <= pre.next.val

AFTER:

pre -> curr -> old pre.next

O(n^2) time
O(1) extra space
"""
class Solution2:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        header = ListNode() # dummy header node for new linked list
        curr = head # the node from original list to be inserted

        while curr:
            # save so we can update curr at end of loop
            next = curr.next

            # find where to insert
            pre = header # insert node between pre and pre.next
            while pre.next and pre.next.val < curr.val:
                pre = pre.next

            # insert between pre and pre.next
            curr.next = pre.next
            pre.next = curr

            # update curr using saved "next"
            curr = next

        return header.next

"""
Solution 2b: optimized to be much faster.

"pre" is not reset to header unless we have to.

"""
class Solution2b:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        header = ListNode() # dummy header node for new linked list
        curr = head # the node from original list to be inserted
        pre = header

        while curr:
            # save so we can update curr at end of loop
            next = curr.next

            # find where to insert
            if (not pre.next) or (pre.next.val >= curr.val):
                pre = header

            while pre.next and pre.next.val < curr.val:
                pre = pre.next

            # insert between pre and pre.next
            curr.next = pre.next
            pre.next = curr

            # update curr using saved "next"
            curr = next

        return header.next

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\narr = {arr}")

        head, _ = build_ll(arr)
        
        res = sol.insertionSortList(head)

        print(f"\n{res}\n")


    sol = Solution() # convert to array, sort, then relink
    
    sol = Solution2() # insertion sort for linked lists
    sol = Solution2b() # optimized

    comment = "LC ex1"
    arr = [4,2,1,3]
    test(arr, comment)

    comment = "LC ex2"
    arr = [-1,5,3,4,0]
    test(arr, comment)

    comment = ""
    arr = [0,-5,5]
    test(arr, comment)
