"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll

###############################################################################
"""
Solution: use 2 pointers, iterative, use dummy header node.

Sorted merge of l1 and l2, each of which is sorted.
Don't create new list nodes.

O(m+n) time
O(1) extra space
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
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

        if l1:
            node.next = l1
        elif l2:
            node.next = l2

        return header.next

###############################################################################
"""
Solution 2: recursion

O(m+n) time
O(1) extra space
"""
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

###############################################################################
"""
Solution 3: iterative w/o using dummy header node.
"""
class Solution3:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
        # This initial part could be simplified by using a dummy header node.
        if (l1 is None) and (l2 is None):
            return None

        if (l2 is None) or (l1 and (l1.val <= l2.val)):
            head = ListNode(l1.val)
            l1 = l1.next
        else: # l2 is not None, and l1.val > l2.val
            head = ListNode(l2.val)
            l2 = l2.next

        tail = head

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next

            tail = tail.next

        if l1: # other list l2 is None
            while l1:
                tail.next = ListNode(l1.val)
                tail = tail.next
                l1 = l1.next

        elif l2: # other list l1 is None
            while l2:
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next

        #return head, tail
        return head

###############################################################################

if __name__ == "__main__":
    def test(arr1, arr2, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\narr1 = {arr1}")
        print(f"arr2 = {arr2}")

        head1, _ = build_ll(arr1)
        head2, _ = build_ll(arr2)
        
        res = sol.mergeTwoLists(head1, head2)

        print(f"\n{res}\n")


    sol = Solution() # iterative
    #sol = Solution2() # recursive
    #sol = Solution3() # iterative w/o using dummy header node; builds new list

    comment = "LC ex; answer = 1,1,2,3,4,4"
    arr1 = [1,2,4]
    arr2 = [1,3,4]
    test(arr1, arr2, comment)

    comment = "one empty list"
    arr1 = [1,2,4]
    arr2 = []
    test(arr1, arr2, comment)

    comment = "two empty lists"
    arr1 = []
    arr2 = []
    test(arr1, arr2, comment)
