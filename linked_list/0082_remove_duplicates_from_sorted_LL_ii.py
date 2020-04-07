"""
82. Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
Solution:

Differences from keeping one node from each sublist of duplicates:
1. Use dummy header node.
2. Use anchor node.
3. Loop is over anchor nodes rather than first node of each sublist to check.
4. Need to check whether to increment node at end of loop.

O(n) time
O(1) extra space
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        header = ListNode() # dummy header node, in case head has dups
        header.next = head

        anchor = header # anchor node in case we need to relink to skip duplicates

        while anchor and anchor.next:
            first = anchor.next # first node to check for duplicates

            scout = first.next # node to increment to check for duplicates
            while scout and scout.val == first.val:
                scout = scout.next

            if scout != first.next: # "first" had duplicates
                anchor.next = scout
                # May still need this anchor if a 2nd sequence of duplicates 
                # follows, so don't increment anchor yet.

            else: # "first" has no duplicates, so can increment anchor
                anchor = anchor.next

        return header.next

###############################################################################
"""
Solution 2:

At start of loop, head acts as "first" node (after anchor node) of potential 
duplicates. In each iteration, there are 2 cases:

1. head has dups: inc head to first node after current sublist of dups.
Then set pre.next to this new head (ie, skip over all the dups just found).

2. head has no dups: just increment pre and head.

O(n) time
O(1) extra space
"""
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        header = ListNode() # dummy header node, in case head has dups
        header.next = head

        pre = header # acts as the anchor node, last node w/ no dups

        while head and head.next:
            if head.val == head.next.val: # head has dups
                while head.next and head.val == head.next.val:
                    head = head.next
                
                head = head.next # next node after current sublist of dups
                pre.next = head
            
            else: # head has no dups, so just increment pre and head
                pre = head # pre.next
                head = head.next

        return header.next

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        head, _ = build_ll(arr)

        print()
        print(head)
        
        res = sol.deleteDuplicates(head)

        print(f"\nAfter: {res}\n")


    sol = Solution()
    sol = Solution2()
    
    comment = "LC ex1; answer = 1, 2, 5"
    arr = [1,2,3,3,4,4,5]
    test(arr, comment)

    comment = "LC ex2; answer = 2, 3"
    arr = [1,1,1,2,3]
    test(arr, comment)

    comment = "single elt"
    arr = [1]
    test(arr, comment)

    comment = "empty list"
    arr = []
    test(arr, comment)

    comment = "list with only duplicates"
    arr = [1,1]
    test(arr, comment)
