"""
230. Kth Smallest Element in a BST
Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution 1: inorder traversal using recursion.

This version uses nonlocal "count" and "res".

O(n) time - or is it more accurately O(max(h, k)) ?
- Because it's inorder, we have to traverse to at least the first leaf,
which takes O(h) time, where h = height of BST, regardless of k. In worst case
of linear BST, this is always O(n) time, regardless of k.

O(h) extra space for recursion

"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            nonlocal count, res

            #if (not node) or (count > k):
            if (not node) or res:
                #print(f"\nnot node or count > k: count = {count}")
                return

            inorder(node.left)
            
            if count == k:
                res = node.val
            
            #print(f"\nnode.val = {node.val}: count = {count}")
            count += 1
            
            inorder(node.right)

        count = 1
        res = None

        inorder(root)
        
        return res

"""
Solution 1b: same, but use nonlocal "k" instead of "count".
"""
class Solution1b:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            nonlocal k, res

            #if (not node) or (k < 0):
            if (not node) or res:
                return

            inorder(node.left)
            
            k -= 1

            if k == 0:
                res = node.val

            inorder(node.right)

        res = None

        inorder(root)
        
        return res

"""
Solution 1c: same, but use nonlocal "res", and use "count" as parameter.
"""
class Solution1c:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node, count=0):
            nonlocal res
            
            #if (not node) or (count > k):
            if (not node) or res:
                return count

            count = inorder(node.left, count)

            count += 1
            if count == k:
                res = node
                return count # optional

            return inorder(node.right, count)

        res = None
        inorder(root)
        
        return res.val

"""
Solution 1d: same, but don't use nonlocal vars.
"""
class Solution1d:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node, count=0, res=None):
            #if (not node) or (count > k):
            if (not node) or res:
                return count, res

            count, res = inorder(node.left, count, res)
            #if res: return count, res # optional

            count += 1
            if count == k:
                res = node
                #return count, node # optional
            
            return inorder(node.right, count, res)

        #res = None
        #_, res = inorder(root, 0, res)
        #return res.val
    
        #_, res = inorder(root)
        return inorder(root)[1].val

###############################################################################
"""
Solution 2: inorder traversal using iteration w/ stack.

O(h + k) time, where h is height of tree.
O(h) extra space due to stack
"""
class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        return None

###############################################################################
"""
Follow-up: What if the BST is modified (insert/delete operations) often and 
you need to find the kth smallest frequently? How would you optimize the 
kthSmallest routine?

Insert and delete in a BST take O(h) time, where h is the height of the tree.
For a balanced tree, h = log n.

### Way 1

Use a BST and a sorted doubly-linked list. Each node in the BST contains
a pointer to a node in the linked list with the same value.

We get O(h) time for insert and delete, and O(k) time for search of kth smallest element.

Insert: insert in BST takes O(h) time. Use parent's pointer to linked list 
node to insert new linked list node, which takes O(1) time.

Delete: delete from BST takes O(h) time. Use pointer to linked list node to 
delete linked list node, which takes O(1) time.

Search: just do linear search of linked list, which takes O(k) time.

Q: how is this better than just using the BST by itself?
Search is strictly O(k) time with a doubly linked list instead of O(n) for 
recursion on BST, or O(h+k) for iteration using a stack.

Not sure--for recursion, is it more accurately O(max(h, k)) time?

########################
### Way 2 (not optimal)

Augment each BST node with number of tree values less than current node value.
When inserting or deleting a node, update this attribute.
Search for kth smallest takes O(h) time.

But can take O(n) time to update values in BST?

########################
### Way 3

Augment each BST node with the size of its left subtree...

index of current node = 1 + (size of left subtree) + (index of parent if right child)


"""

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        root = array_to_bt_lc(arr)

        print(arr)
        print(f"k = {k}\n")
        print_tree(root)
       
        res = sol.kthSmallest(root, k)

        print(f"\nresult: {res}\n")
        
    sol = Solution() # inorder traversal using recursion; nonlocal vars "res" and "count"
    sol = Solution1b() # same, but use nonlocal "k" instead of "count".
    sol = Solution1c() # same, but use nonlocal "res", and use "count" as parameter.
    sol = Solution1d() # same, but don't use nonlocal vars

    sol = Solution2() # inorder traversal using iteration w/ stack.

    comment = "LC example 1; answer = 1"
    arr = [3,1,4,None,2]
    k = 1
    test(arr, k, comment)

    comment = "LC example 2; answer = 3"
    arr = [5,3,6,2,4,None,None,1]
    k = 3
    test(arr, k, comment)
