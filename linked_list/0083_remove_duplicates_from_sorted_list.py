"""
83. Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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
Solution: use 2 pointers:
node = last node found with no dups; acts as anchor
cur = scouts ahead for next node that is not equal in value to node

O(n) time
O(1) extra space
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:       
        node = head

        while node: # last node found with no dups; acts as anchor
            cur = node.next # first node after "node" to check for dups
            # scout ahead for first node not equal in value to "node"
            while cur and cur.val == node.val:
                cur = cur.next

            node.next = cur
            node = node.next

        return head

###############################################################################
"""
Solution 2: same idea as sol 1, but use cur and cur.next.

O(n) time
O(1) extra space
"""
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:       
        cur = head

        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head

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

        print(f"\n{res}\n")


    sol = Solution()
    sol = Solution2()
    
    comment = "LC ex1"
    arr = [1,1,2]
    test(arr, comment)

    comment = "LC ex2"
    arr = [1,1,2,3,3]
    test(arr, comment)
