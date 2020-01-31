"""
109. Convert Sorted List to Binary Search Tree
Medium

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

import sys
sys.path.insert(1, '../tree/')
sys.path.insert(1, '../linked_list/')

from binary_tree import TreeNode, print_tree #, array_to_bt
from linked_list import ListNode, build_ll

###############################################################################
"""
Solution #1: recursion by passing head and count of current sublist.  
Don't convert linked list to array.

n/2 time to find first mid
2*(n/4) = n/2 time to find the 2 mids at 2nd level of recursion
4*(n/8) = n/2 time to find the 4 mids at 3rd level of recursion
etc.
O(log n) levels of recursion since tree is height-balanced

Total time = (log n)*(n/2) = O(n log n)

O(n log n) time
O(n) extra space for tree that is built and returned
O(log n) for recursion stack since tree is height-balanced
"""
def build_bst(head):
    def build(head, count):
        #if (not head) or (count == 0):
        if count == 0:
            return None

        mid = head
        mid_count = count // 2 # tree is left-biased
        #mid_count = (count - 1) // 2 # tree is right-biased

        for _ in range(mid_count):
            mid = mid.next

        root = TreeNode(mid.val)
        root.left = build(head, mid_count)
        root.right = build(mid.next, count - mid_count - 1)

        return root

    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    return build(head, count)

"""
count = 1 
mid_count = 0
root = mid = head
root.left = build(head, 0) # returns None
root.right = build(mid.next, 1 - 0 - 1 = 0) # returns None

count = 2
mid_count = 1
root = mid = head.next # 2nd of 2 elts
root.left = build(head, 1) # returns 1st of 2 elts
root.right = build(None, 2 - 1 - 1 = 0) # returns None
"""

###############################################################################
"""
Solution #2: inorder construction of BST while traversing linked list.

Traversal of the sorted linked list visits the values in the same order as an
inorder traversal of any BST corresponding to the sorted values.
So we can do an inorder construction of the BST while travering the linked
list at the same time.

Recursively:
The first element of the list is the leftmost descendant of the root.
When the left half is built, the "head" in the linked list is pointing at
the middle node of the list, which is used to create the root of the tree.
The remaining nodes of the list are used to build the right subtree.

O(n) time
O() extra space
"""
def build_bst2(head):
    def build(low, high):
        nonlocal head

        if low > high:
            return None

        mid = (low + high) // 2 # tree is right-biased
        #mid = (low + high + 1) // 2 # tree is left-biased

        left = build(low, mid-1)
        
        root = TreeNode(head.val)
        root.left = left

        head = head.next
        
        root.right = build(mid+1, high)
        
        return root
    
    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    return build(0, count-1)

###############################################################################

if __name__ == "__main__":
    def test(arr):
        head, _ = build_ll(arr)
        
        #root = build_bst(head)
        root = build_bst2(head)

        print("#"*80)
        print(arr)
        print()
        print_tree(root)

    arrays = [
        [],
        [0],
        [1],
        [1,2],
        [1,2,3],
        [1,2,3,4],
        [1,2,3,4,5],
        [1,2,3,4,5,6,7,8,9],
        [-10,-3,0,5,9], # LC
    ]

    for arr in arrays:
        test(arr)
