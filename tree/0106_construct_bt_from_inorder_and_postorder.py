"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree #, array_to_bt

###############################################################################
"""
Idea:
1. postorder: last element is the root.  The remaining elements are grouped
by whether they are in the left or right subtree.  In particular, the second
to the last element is root's right child.

2. inorder: all elements to left of root are in left subtree;
all elements to right of root are in right subtree.

3. Build right subtree first...

Example:
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

postorder:
    root = 3
    remaining = [9][15,7,20]

inorder:
    [9]3[15,20,7]

"""
###############################################################################
"""
Solution #1: recursion...

Cons:
- Modifies input "postorder"
- inorder.index(root.val) takes O(n) time
- recursive steps take O(n) time and extra space
- overall time O(n^2), space O(n^2)

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
"""
def build_bt(inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder.pop()) # modifies "postorder"
    r = inorder.index(root.val) # O(n) time
    
    root.right = build_bt(inorder[r+1:], postorder) # O(n) time and extra space
    root.left = build_bt(inorder[:r], postorder) # O(n) time and extra space

    return root

###############################################################################
"""
Solution #2:

O(n) time
O(n) extra space

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.
"""
def build_bt2(inorder, postorder):
    inorder_dict = {}
    postorder = postorder[:] # in order to not modify input postorder

    for i, val in enumerate(inorder):
        inorder_dict[val] = i

    def build(low, high):
        if low > high:
            return None

        root = TreeNode(postorder.pop())
        mid = inorder_dict[root.val]

        root.right = build(mid+1, high)
        root.left = build(low, mid-1)
        
        return root

    return build(0, len(inorder)-1)

###############################################################################
"""
Solution #3: O(n) recursive sol w/o using index() or dict.

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34802/O(n)-recursive-solution-without-hashmap-nor-index
"""
def build_bt3(inorder, postorder):
    inorder = inorder[:]
    postorder = postorder[:]

    def post_dfs(stop):
        if postorder and inorder[-1] != stop:
            root = TreeNode(postorder.pop())
            
            root.right = post_dfs(root.val)
            
            inorder.pop()
            
            root.left = post_dfs(stop)
            
            return root

    return post_dfs(None)

###############################################################################

if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    
    print(f"\ninorder = {inorder}")
    print(f"postorder = {postorder}\n")

    root = build_bt(inorder, postorder)
    print_tree(root)
    print(f"\nAFTER: inorder = {inorder}")
    print(f"AFTER: postorder = {postorder}\n")

    print("#"*80)
    postorder = [9,15,7,20,3]
    root = build_bt2(inorder, postorder)
    print_tree(root)
    print(f"\nAFTER: inorder = {inorder}")
    print(f"AFTER: postorder = {postorder}\n")

    print("#"*80)
    postorder = [9,15,7,20,3]
    root = build_bt3(inorder, postorder)
    print_tree(root)
    print(f"\nAFTER: inorder = {inorder}")
    print(f"AFTER: postorder = {postorder}\n")



