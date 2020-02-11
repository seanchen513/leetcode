"""
"""

from typing import List
import collections

"""
Union find with no path compression and no union by rank/height.
If there are n elements in the set, assume the elements are the integers
0, 1, 2, ..., n-1.

Naive union find operations take O(n) time.
Can be improved to O(log n) using union by rank or height.
"""
class SimpleUnionFind:
    def __init__(self, n):
        self.n = n # number of disjoint subsets
        self.par = [0]*n
        
        # Initialize every element to be in its own singleton set.
        for i in range(n): 
            self.par[i] = i

    # No path compression, so O(n) time.  Iterative.
    def find(self, x):
        while self.par[x] != x:
            x = self.par[x]

        return x
    
    def union(self, x, y):
        px = self.par(x)
        py = self.par(y)

        if px != py:
            self.par[px] = py
            self.n -= 1 # number of disjoint subsets has decreased by one

        return py # representative of the union

    def same_subset(self, x, y):
        return self.find(x) == self.find(y)

###############################################################################
"""
Union find with path compression and union by rank.
If there are n elements in the set, assume the elements are the integers
0, 1, 2, ..., n-1.
"""
class UnionFind:
    def __init__(self, n):
        self.n = n # number of disjoint subsets
        self.par = [0]*n
        
        # Initialize every element to be in its own singleton set.
        for i in range(n): 
            self.par[i] = i

        self.rank = [0]*n

    """
    Recursive find() w/ path compression.
    Finds and returns the representative of the set that the given element is in.
    Recursively calls itself until a fixed point (x such that par[x] = x) is found.
    That fixed point is the representative of the set.  As the recursion unwinds,
    the representative is assigned to be the parent of x and all elements that were 
    encountered along the way.
    """
    def find(self, x):
        if self.par[x] == x: 
            return x
        
        self.par[x] = self.find(self.par[x])
        
        return self.par[x]

    """
    Iterative find() w/ path compression.
    """
    def find2(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x

    """
    Union by Rank:
    Attach smaller rank tree to parent of higher rank tree.  If ranks are the
    same, then make one the parent and increment its rank by one.
    """
    def union(self, x, y):
        px = self.par[x]
        py = self.par[y]

        if px == py:
            return px

        self.n -= 1 # number of disjoint subsets has decreased by one

        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            return px
    
        self.par[px] = py

        if self.rank[px] == self.rank[py]:
            self.rank[py] += 1

        return px

    def same_subset(self, x, y):
        return self.find(x) == self.find(y)

###############################################################################
"""
Use union find to check if a graph is cyclic.
"""
def is_cyclic(n : int, edges: List[List[int]]) -> bool:
    graph = {i: [] for i in range(n)}
    for x, y in edges:
        graph[x] += [y]

    uf = UnionFind(n)

    for x in graph:
        px = uf.find(x)
        
        for y in graph[x]:
            py = uf.find(y)

            if px == py:
                return True
            
            uf.union(px, py)

    return False

###############################################################################

if __name__ == "__main__":
    def test(n, edges, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")
        print(edges)

        res = is_cyclic(n, edges)

        if res:
            print("\nGraph contains a cycle.")
        else:
            print("\nGraph does not contain a cycle.")


    comment = "Empty graph: no nodes or edges"
    edges = []
    n = 0
    test(n, edges, comment)

    comment = "Single node with no edges"
    edges = []
    n = 1
    test(n, edges, comment)

    comment = "Single node with self-loop"
    edges = [[0,0]]
    n = 1
    test(n, edges, comment)

    comment = "Multiple nodes with no edges"
    edges = []
    n = 5
    test(n, edges, comment)

    comment = "Cyclic graph"
    edges = [[0,1],[1,2],[2,0]]
    n = 3
    test(n, edges, comment)

    comment = "Linear graph"
    edges = [[0,1],[1,2],[2,3]]
    n = 4
    test(n, edges, comment)
