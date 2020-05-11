"""
1443. Minimum Time to Collect All Apples in a Tree
Medium

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = True means that vertex i has an apple, otherwise, it does not have any apple.

Example 1:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 2:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]
Output: 0

Constraints:

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""

from typing import List

###############################################################################
"""
Solution: build parents dict from edges. For each node with apple, traverse
up parents path until we hit a previously visited node.

* can use parents array rather than dict since nodes are 0..n-1.

O(n) time
O(n) extra space: for parents dict
"""
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        par = {}
        
        for x, y in edges:
            par[y] = x

        count = 0
        visited = set()

        for x, apple in enumerate(hasApple):
            if apple:
                y = x
                while y in par and y not in visited:
                    count += 2
                    visited.add(y)
                    y = par[y]
                    
        return count

"""
Solution 1b: same, but avoid using visited set by deleting a node's entry in
the parents dict after it has been visited.

O(n) time
O(n) extra space: for parents dict
"""
class Solution1b:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        par = {}
        
        for x, y in edges:
            par[y] = x

        count = 0

        for x, apple in enumerate(hasApple):
            if apple:
                y = x
                while y in par:
                    count += 2
                    temp = y
                    y = par[y]
                    del par[temp]
                    
        return count

###############################################################################
"""
Solution 2: don't assume 0 is root, and treat tree as undirected graph.
Build graph dict or list from edges, use visited set, and use DFS recursion.

O(n) time
O(V+E) = O(n) extra space: for graph dict or list (V = n, E = n-1)
"""
class Solution2:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            count = 0

            for nbr in d[node]:
                count += dfs(nbr)

            if count > 0:
                return count + 2

            if hasApple[node]:
                return 2

            return 0

        #d = collections.defaultdict(list)
        d = [[] for _ in range(n)]

        for x, y in edges:
            d[x].append(y)
            d[y].append(x)

        visited = set()

        # Subtract 2 because root doesn't have a parent.
        return max(dfs(0) - 2, 0)

"""
If an actual tree data structure was given, we could do something like the
following:

def dfs(node):
    if not node or node in visited:
        return 0

    visited.add(node)

    left = dfs(node.left)
    right = dfs(node.right)

    if left or right:
        return left + right + 2

    return 0

"""
###############################################################################

if __name__ == "__main__":
    def test(n, edges, hasApple, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"edges = {edges}")
        print(f"hasApple = {hasApple}")

        res = sol.minTime(n, edges, hasApple)

        print(f"\nres = {res}\n")


    sol = Solution() # use parents dict
    sol = Solution1b() # same, but delete dict entries after node visited

    sol = Solution2() # treat as undirected graph

    comment = "LC ex1; answer = 8"
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    test(n, edges, hasApple, comment)

    comment = "LC ex2; answer = 6"
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,False,True,False]
    test(n, edges, hasApple, comment)

    comment = "LC ex3; answer = 0"
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,False,False,False,False,False]
    test(n, edges, hasApple, comment)

    comment = "LC Albertplus007; answer = 4"
    n = 3
    edges = [[0,2],[1,2]]
    hasApple = [False,True,False]
    test(n, edges, hasApple, comment)
    
    comment = "LC hiepit; answer = 4"
    n = 4
    edges = [[0,2],[0,3],[1,2]]
    hasApple = [False,True,False,False]
    test(n, edges, hasApple, comment)
