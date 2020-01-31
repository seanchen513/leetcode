"""
236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

from binary_tree import print_tree, array_to_bt

###############################################################################
"""
Solution #1: Find paths from root to each node, then compare paths and
return last common node.
"""
def lca_bt(root, p, q):
    def path_to_node(root, node, path):
        if not root:
            return None

        if (root == node
            or path_to_node(root.left, node, path) 
            or path_to_node(root.right, node, path)
        ):
            path.append(root)
            #path += [root]
            #path = path + [root] # doesn't work
            
            return path

        return None

    path1 = path_to_node(root, p, [])[::-1]
    path2 = path_to_node(root, q, [])[::-1]
    
    #print(f"\npath1 = {[node.val for node in path1]}")
    #print(f"path2 = {[node.val for node in path2]}")

    i = 0
    n = min(len(path1), len(path2))
    prev = None

    while i < n and path1[i] == path2[i]:
        prev = path1[i]
        i += 1

    return prev

"""
Solution #1b: same as sol #1, but instead of reversing paths,
traverse the first path and build a set of nodes,
then traverse the second path and check against the set.
"""
def lca_bt1b(root, p, q):
    def path_to_node(root, node, path):
        if not root:
            return None

        if (root == node
            or path_to_node(root.left, node, path) 
            or path_to_node(root.right, node, path)
        ):
            path.append(root)
            return path

        return None

    path1 = path_to_node(root, p, [])
    path2 = path_to_node(root, q, [])
    
    #print(f"\npath1 = {[node.val for node in path1]}")
    #print(f"path2 = {[node.val for node in path2]}")

    s = set(path1)

    for node in path2:
        if node in s:
            return node

    return None # shouldn't happen

"""
DOESNT WORK
"""
def lca_bt1c(root, p, q):
    def path_to_node(root, p, q, path1, path2):
        if not root:
            return None, None

        left, right = path_to_node(root.left, p, q, path1, path2) 

        left, right = path_to_node(root.right, p, q, path1, path2)

        #if root == p or left == p or right == p:
        if p in (root, left, right):
            path1.append(root)   
            return path1, path2

        if q in (root, left, right):
            path2.append(root)   
            return path1, path2

        return None, None

    path1, path2 = path_to_node(root, p, q, [], [])
    path1 = path1[::-1]
    path2 = path2[::-1]
    
    #print(f"\npath1 = {[node.val for node in path1]}")
    #print(f"path2 = {[node.val for node in path2]}")

    i = 0
    n = min(len(path1), len(path2))
    prev = None

    while i < n and path1[i] == path2[i]:
        prev = path1[i]
        i += 1

    return prev

###############################################################################
"""
Solution #2: recursion

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/152682/Python-simple-recursive-solution-with-detailed-explanation
"""
def lca_bt2(root, p, q):
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lca_bt2(root.left, p, q)
    right = lca_bt2(root.right, p, q)

    if left and right:
        return root
    else:
        # (1) If both left and right are None, return None.
        # Neither given nodes found in this subtree.
        # (2) If left is a found node and right is None, return left.
        # (3) If right is a found node and left is None, return right.

        return left or right

"""
Solution #2b:

Same as sol #2 but rewritten to be more concise.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
"""
def lca_bt2b(root, p, q):
    if root in (None, p, q):
        return root

    left, right = (lca_bt2b(kid, p, q) 
        for kid in (root.left, root.right))

    return root if (left and right) else (left or right)

###############################################################################
"""
Solution #3: iteration by creating parents dict

Can think of the parents dict as a way of storing the paths for p and
q in a single data structure.

Can also use a queue instead of a stack.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
"""
def lca_bt3(root, p, q):
    ### Build parents dict until both given nodes are included.
    stack = [root]
    parents = {root: None}

    while (p not in parents) or (q not in parents):
        node = stack.pop()

        if node.left:
            parents[node.left] = node
            stack.append(node.left)

        if node.right:
            parents[node.right] = node
            stack.append(node.right)

    ### Create set of nodes from None->root to p
    ancestors = set()

    while p:
        ancestors.add(p)
        p = parents[p]

    ### Traverse path from q to root->None, checking against set
    while q not in ancestors:
        q = parents[q]

    return q

###############################################################################

if __name__ == "__main__":
    def test(root, p, q):
        print("\n" + "#"*80)
        print_tree(root)

        print(f"\np = {p.val}")
        print(f"q = {q.val}")
        
        lca = lca_bt(root, p, q)
        lca1b = lca_bt1b(root, p, q)
        #lca1c = lca_bt1c(root, p, q)
        lca2 = lca_bt2(root, p, q)
        lca2b = lca_bt2b(root, p, q)
        lca3 = lca_bt3(root, p, q)

        print(f"\nLCA (sol #1)  = {lca.val}")
        print(f"LCA (sol #1b) = {lca1b.val}")
        #print(f"\nLCA (sol #1c) = {lca1c.val}")
        print(f"LCA (sol #2)  = {lca2.val}")
        print(f"LCA (sol #2b) = {lca2b.val}")
        print(f"LCA (sol #3)  = {lca3.val}")
    
    # LC ex1
    arr = [3, 5,1, 6,2,0,8, None,None,7,4,None,None]
    nodes = array_to_bt(arr)
    root = nodes[0]
    p = nodes[arr.index(5)]
    q = nodes[arr.index(1)]
    #p = bt_find(root, 5)
    #q = bt_find(root, 1)
    test(root, p, q)

    # LC ex2
    #q = bt_find(root, 4)
    q = nodes[arr.index(4)]
    test(root, p, q)
