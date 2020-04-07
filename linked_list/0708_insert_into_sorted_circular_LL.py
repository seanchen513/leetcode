"""
708. Insert into a Sorted Circular Linked List
Medium

Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

Example 1:
 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]

Constraints:

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_circular_ll, build_ll, print_circular_ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################################################################
"""
Solution: 

Cases:
0. empty list
1. min <= x <= max: add x b/w prev and curr
2. x outside range of [min, max]: add x after tail (max): tail > tail.next
    - tail is found when we've almost looped entire list and have: 
        - pre = tail (max)
        - cur = head (min)
        - pre.val > cur.val
    - if x < min: x < cur.val
    - if x > max: x > pre.val
3. all list values are equal; we've looped entire list 
    - add x anywhere

https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/solution/

O(n) time
O(1) extra space
"""
class Solution:
    #def insert(self, head: 'Node', insertVal: int) -> 'Node':
    def insert(self, head: ListNode, x: int) -> ListNode:
        if not head: # case 0: empty list
            head = ListNode(x)
            head.next = head
            return head
        
        pre = head
        cur = head.next
        
        while 1:
            if pre.val <= x <= cur.val: # case 1: insert in middle
                break
            
            if pre.val > cur.val: # case 2: pre is tail (max), cur is head (min)
                if x > pre.val or x < cur.val:
                    break

            pre = cur
            cur = cur.next
            
            if pre == head: # case 3: we've looped around once; all elts equal
                break

        pre.next = ListNode(x, cur)
        return head

"""
Solution 2: same idea, but use one pointer.

case 0: empty list
case 1: insert in middle: min <= x <= max
case 2: insert at end: x < min or x > max
case 3: all values in list equal, so can insert anywhere; insert at end
"""
class Solution2:
    def insert(self, head: ListNode, x: int) -> ListNode:
        if not head: # case 0: empty list
            head = ListNode(x)
            head.next = head
            return head
        
        pre = head
        
        while 1:
            if pre.val <= x <= pre.next.val: # case 1: insert in middle
                break
            
            if pre.val > pre.next.val and (x > pre.val or x < pre.next.val): 
                # case 2: pre is tail (max), cur is head (min)
                break
            
            if pre.next == head: # case 3: we've looped around once; all elts equal
                break

            pre = pre.next

        pre.next = ListNode(x, pre.next)
        return head

###############################################################################
"""
Solution 3: same as sol 2, but move case 1 into the while loop condition.
"""
class Solution3:
    def insert(self, head: ListNode, x: int) -> ListNode:
        # case 0: empty list
        if not head:
            head = ListNode(x)
            head.next = head
            return head
        
        pre = head
        
        while not (pre.val <= x <= pre.next.val): # not case 1: insert in middle
            if pre.val > pre.next.val and (x > pre.val or x < pre.next.val): 
                # case 2: pre is tail (max), cur is head (min)
                break
            if pre.next == head: # case 3: we've looped around once; all elts equal
                break

            pre = pre.next

        pre.next = ListNode(x, pre.next)
        return head

###############################################################################

if __name__ == "__main__":
    def test(arr, x, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\narr = {arr}")
        print(f"x = {x}")

        head, _ = build_circular_ll(arr, 0)
        #head, tail = build_ll(arr)
        #tail.next = head
        
        res = sol.insert(head, x)
        print(f"\nres.val = {res.val}")

        #print(f"\n{res}\n")
        print_circular_ll(res)
        print('\n')


    sol = Solution()
    
    comment = "LC ex1"
    arr = [3,4,1]
    x = 2
    test(arr, x, comment)

    comment = "LC ex2"
    arr = []
    x = 1
    test(arr, x, comment)

    comment = "LC ex3"
    arr = [1]
    x = 0
    test(arr, x, comment)

    comment = "LC TC"
    arr = [3,5,1]
    x = 0
    test(arr, x, comment)
