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

from binary_tree import TreeNode, print_tree, array_to_bt

###############################################################################
"""
Solution #1: Find paths from root to each node, then compare paths and
return last common node.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
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
class Solution1b:
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

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

        s = set(path1)

        for node in path2:
            if node in s:
                return node

        return None # shouldn't happen

###############################################################################
"""
Solution #2: recursion

Return value is the LCA for that subtree.

Base cases:
    Node is None or is one of the given nodes: return itself

Induction step:
    1. If both left and right are None, return None.
    Neither given nodes found in this subtree.
    2. If node(s) found on left, but right is None, return left LCA.
    3. If node(s) found on right, but left is None, return right LCA.
    4. If one node found on left, and other node on right, then
    return node itself, as it is the LCA of its subtree.

O(n) time
O(h) extra space

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/152682/Python-simple-recursive-solution-with-detailed-explanation
"""
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root, p, q):
            if not root or root == p or root == q:
                return root

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root
            else:
                return left or right

        return lca(root, p, q)

"""
Solution #2b:

Same as sol #2 but rewritten to be more concise.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
"""
class Solution2b:
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root, p, q):
            if root in (None, p, q):
                return root

            L, R = (lca(kid, p, q) for kid in (root.left, root.right))

            return root if (L and R) else (L or R)

        return lca(root, p, q)

###############################################################################
"""
Solution #3: iteration by creating parents dict

Can think of the parents dict as a way of storing the paths for p and
q in a single data structure.

Can also use a queue instead of a stack.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
"""
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', 
        p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

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
        solutions = [Solution(), Solution1b(), Solution2(), Solution2b(), 
            Solution3()]

        lca = [s.lowestCommonAncestor(root, p, q).val for s in solutions]

        print("#"*80)
        print_tree(root)

        print(f"\np = {p.val}")
        print(f"q = {q.val}")
        
        print(f"\nLCA (all solutions) = {lca}\n")

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
