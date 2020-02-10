"""
207. Course Schedule
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false

Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List
import collections

###############################################################################
"""
Solution 1: DFS using recursive is_cyclic(), and visited and rec_stack arrays.
Could also use rec_stack as a set.

? O(V+E) time: 
    Creating adjacency list from list of edges is O(E).  
    ***

O(V+E) extra space:
    O(V) for visited and rec_stack arrays.
    O(E) for adjacency list.
"""
class Solution:
    #def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        def is_cyclic(v):
            visited[v] = 1
            rec_stack[v] = 1 # add current node to recursion stack

            for nbr in graph[v]:
                if not visited[nbr]:
                    if is_cyclic(nbr):
                        return True
                elif rec_stack[nbr]:
                    return True
            
            # pop current node from recursion stack
            rec_stack[v] = 0
            return False

        visited = [0] * n
        rec_stack = [0] * n # recursion stack
        
        graph = {i: [] for i in range(n)}
        for x, y in prereqs:
            graph[x] += [y]
        
        for v in graph: # or range(n)
            if not visited[v]:
                if is_cyclic(v):
                    return False # cyclic, so can't finish all courses

        return True # not cyclic, so can finish all courses

###############################################################################
"""
Solution 2: DFS using recursive is_cyclic(), and use "visited" array to 
track 3 states (for each node).  This is essentially the same as doing DFS with
visited and recursion stack arrays.

Can think of as 3 colors:

0 = unvisited (WHITE)
1 = visiting and in recursion stack (BLACK)
2 = visited but not in recursion stack (GRAY)
"""
class Solution2:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        def is_cyclic(v):
            # mark visited and add to recursion stack
            visited[v] = 1 # GREY STATE

            for nbr in graph[v]:
                if not visited[nbr]:
                    if is_cyclic(nbr):
                        return True
                elif visited[nbr] == 1: # nbr in recursion stack
                    return True
            
            # pop current node from recursion stack
            visited[v] = 2 # BLACK state
            return False

        visited = [0] * n # 0 = unvisited; WHITE states
        
        graph = {i: [] for i in range(n)}
        for x, y in prereqs:
            graph[x] += [y]

        for v in graph: # or range(n)
            if not visited[v]:
                if is_cyclic(v):
                    return False # cyclic, so can't finish all courses

        return True # not cyclic, so can finish all courses

###############################################################################
"""
Solution 3: Attempt BFS topological sorting using two lists and a counter.
Use degree array rather than back array.

Start with nodes that have 0 in-degree, ie, there are no edges from
other nodes leading to it.

This is same as BFS from front to end, starting with nodes where
backward[node] is empty.  Equivalent statements made in comments.

front -> ... -> end

O(V+E) time
O(V+E) extra space

Runtime: 88 ms, faster than 99.14% of Python3 online submissions
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        degree = [0] * n

        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            degree[y] += 1 # in-degree; ie, "backward[y] = [x]"

        # Start with nodes of degree 0.
        level = [i for i in range(n) if degree[i] == 0] # ie, if not backward[i]
        
        # Count of nodes with degree 0 or updated to have degree 0.
        # Ie, count of nodes with backward[i] empty or popped from backward
        count = len(level) 

        while level and count != n: 
            next_level = []

            for i in level:
                ### Can also increment and check count here
                #count += 1
                #if count == n:
                #    return True # no cycles, can finish all courses

                for j in graph[i]: # ie, for nbr in forward[i]
                    degree[j] -= 1 # ie, backward[nbr].remove(i)

                    if degree[j] == 0: # ie, if not backward[nbr]
                        count += 1 
                        if count == n:
                            return True # no cycles, can finish all courses

                        next_level.append(j)

            level = next_level
        
        # Needed for False cases, as well as True trivial case:
        # n=1, count=1, prereqs=[] (1 vertex with no edges)
        #return count == n
        return sum(degree) == 0

"""
Solution 3b: BFS using deque, front to end, degree array rather than back array.
Same as sol #3, but use deque instead of 2 lists
"""
class Solution3b:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        degree = [0] * n

        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            degree[y] += 1 # in-degree; ie, "backward[y] = [x]"

        # Start with nodes of degree 0.
        q = collections.deque(i for i in range(n) if degree[i] == 0) # ie, if not backward[i]
        
        # Count of nodes with degree 0 or updated to have degree 0.
        # Ie, count of nodes with backward[i] empty or popped from backward
        #count = len(q) 

        while q:
            node = q.popleft()

            for nbr in graph[node]: # ie, for nbr in forward[i]
                degree[nbr] -= 1 # ie, backward[nbr].remove(i)

                if degree[nbr] == 0: # ie, if not backward[nbr]
                    #count += 1 # count here to short circuit early
                    #if count == n: # short circuit
                    #    return True # no cycles, can finish all courses

                    q.append(nbr)

        #return count == n
        return sum(degree) == 0 # no cycles

###############################################################################
"""
Solution 3c: BFS using deque, front to end, using back array rather than
degree array.
"""
class Solution3c:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        back = collections.defaultdict(list)

        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            back[y] += [x]

        # Start with nodes with no back link (in-degree 0).
        q = collections.deque(i for i in range(n) if not back[i])
        #count = len(q)

        while q:
            node = q.popleft()
            # can increment count here instead if initialize count with 0
            
            for nbr in graph[node]:
                back[nbr].remove(node) # remove back link from nbr->node

                if not back[nbr]:
                    #count += 1
                    q.append(nbr)
            
            back.pop(node) # back[node] is []

        #return count == n
        return not back

"""
Solution 3d: BFS using deque, end to front, using back array.
"""
class Solution3d:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        back = collections.defaultdict(list)

        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            back[y] += [x]

        # Start with nodes with no forward links (out-degree 0).
        q = collections.deque(i for i in range(n) if not graph[i])

        while q:
            node = q.popleft()
            
            for nbr in back[node]:
                graph[nbr].remove(node) # remove forward link from node->nbr

                if not graph[nbr]:
                    q.append(nbr)

            graph.pop(node) # graph[node] is []

        return not graph # acyclic if no nodes left with forward links

###############################################################################
"""
Solution 4: DFS with stack, traversing front to end, using degree array rather
than back array.

front -> ... -> end
"""
class Solution4:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        degree = [0] * n
        
        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            degree[y] += 1 # in-degree; ie, "backward[y] = [x]"

        # Start with nodes of degree 0.
        stack = [i for i in range(n) if degree[i] == 0] # ie, if not backward[i]
        
        # Count of nodes with degree 0 or updated to have degree 0.
        # Ie, count of nodes with backward[i] empty or popped from backward
        count = len(stack) 

        while stack:
            node = stack.pop()

            for nbr in graph[node]: # ie, for nbr in forward[i]
                degree[nbr] -= 1 # ie, backward[nbr].remove(i)

                if degree[nbr] == 0: # ie, if not backward[nbr]
                    count += 1
                    #if count == n: # short circuit
                    #    return True # no cycles, can finish all courses

                    stack.append(nbr)

        return count == n
        #return sum(degree) == 0 # no cycles

###############################################################################
"""
Solution 4b: DFS with stack, front to end, back array.
"""
class Solution4b:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # ie, forward
        back = collections.defaultdict(list)
        #graph = {i: set() for i in range(n)} # ie, forward
        #back = collections.defaultdict(set)

        for x, y in prereqs:
            graph[x] += [y] # ie, "forward[x] = y"
            back[y] += [x]            
            #graph[x].add(y)
            #back[y].add(x)
        
        # Start with nodes with no back links (0 in-degree).
        stack = [i for i in range(n) if not back[i]]

        while stack:
            node = stack.pop()

            for nbr in graph[node]:
                back[nbr].remove(node)

                if not back[nbr]:
                    stack.append(nbr)
            
            back.pop(node)

        return not back

###############################################################################
"""
Solution 4c: DFS with stack, end to front, back array.
"""
class Solution4c:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        #graph = {i: [] for i in range(n)} # ie, forward
        #back = collections.defaultdict(list)
        graph = {i: set() for i in range(n)}
        back = collections.defaultdict(set)

        for x, y in prereqs:
            #graph[x] += [y] # ie, "forward[x] = y"
            #back[y] += [x]            
            graph[x].add(y)
            back[y].add(x)

        # Start with nodes with no forward links (0 out-degree).
        stack = [i for i in range(n) if not graph[i]]
        
        while stack:
            node = stack.pop()

            for nbr in back[node]:
                graph[nbr].remove(node) # fast if graph is dict of sets

                if not graph[nbr]:
                    stack.append(nbr)

            graph.pop(node) # graph[node] is []

        return not graph # no cycles

###############################################################################
"""
Solution 5: Use Tarjan's algo for computing strongly connected components (SCC).

A directed graph is acyclic if and only if it has no strongly connected 
subgraphs with more than one vertex.

Any SCC with size > 1 implies a cycle.  
Noncyclic components have a singleton SCC by themself.
Self-loops also have an SCC by themself, so need separate check for self-loops.

O(E+V)
"""
class Solution5:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        pass

###############################################################################

if __name__ == "__main__":
    def test(n, arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        res = s.canFinish(n, arr)

        print(f"\nn = {n}")
        print(f"\n{arr[:20]}")
        #print(f"\nlen(arr) = {len(arr)}")
        #if len(arr) > 20:
        #    print(" (only show at most 20 elements)")

        print(f"\nresult = {res}")


    #s = Solution() # DFS w/ visited and rec_stack
    #s = Solution2() # DFS w/ visitied and 3 states/colors

    ### 3 and 4 variants: attempt topological sorting (Kahn's algo)
    #s = Solution3() # BFS w/ 2 lists, front to end, degree array
    #s = Solution3b() # BFS w/ deque, front to end, degree array
    #s = Solution3c() # BFS w/ deque, front to end, back array
    #s = Solution3d() # BFS w/ deque, end to front, back array

    #s = Solution4() # DFS w/ stack, front to end, degree array
    s = Solution4b() # DFS w/ stack, front to end, back array
    #s = Solution4c() # DFS w/ stack, end to front, back array
    
    ### NOT DONE:
    ###s = Solution5() # Tarjan's algo for strongly connected components

    comment = "LC ex1; answer = True"
    n = 2
    arr = [[1,0]]
    test(n, arr, comment)
    
    comment = "LC ex2; answer = False"
    n = 2
    arr = [[1,0],[0,1]]
    test(n, arr, comment)

    comment = "LC test case; answer = True"
    n = 3
    arr = [[1,0]]
    test(n, arr, comment)

    comment = "LC test case; answer = True"
    n = 1
    arr = []
    test(n, arr, comment)

    comment = "G4G example; answer = True"
    n = 6
    arr = [[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]
    test(n, arr, comment)

    comment = "LC210 ex2; answer = True"
    n = 4
    arr = [[1,0],[2,0],[3,1],[3,2]]
    test(n, arr, comment)
