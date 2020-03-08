"""
1376. Time Needed to Inform All Employees
Medium

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

Example 3:

Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.

Example 4:

Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.

Example 5:

Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076

Constraints:

1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""

from typing import List
import collections

###############################################################################
"""
Solution 1: DFS.  Use subooordinates dict built from manager list.

Runtime: 1344 ms, faster than 90.00% of Python3 online submissions
Memory Usage: 51.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i, total_time):
            nonlocal mx

            if informTime[i] == 0:
            #if subord[i] == []:
                if total_time > mx:
                    mx = total_time
                return

            total_time += informTime[i]

            for j in subord[i]:
                dfs(j, total_time)

        mx = 0 # max inform time

        ### Build adjacency dict of suboordinates (children of node).
        subord = collections.defaultdict(list)        
        for i, mgr in enumerate(manager): # Not used: mgr[-1] = headID
            subord[mgr].append(i)

        ### Alternatively, build adjacency list of children nodes.
        # subord = [[] for _ in range(n)]
        # for i, mgr in enumerate(manager):
        #     if mgr >= 0:
        #         subord[mgr].append(i)
        
        dfs(headID, 0)
                
        return mx

"""
Solution 1b: same as sol 1, but rewritten slightly.
"""
class Solution1b:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i, total_time):
            nonlocal mx

            if informTime[i]:
            #if subord[i]:
                total_time += informTime[i]
                
                for j in subord[i]:
                    dfs(j, total_time)
                
                if total_time > mx:
                    mx = total_time

        mx = 0 # max inform time
        subord = collections.defaultdict(list)
        
        for i, mgr in enumerate(manager): # Not used: mgr[-1] = headID
            subord[mgr].append(i)

        dfs(headID, 0)
                
        return mx

"""
Solution 1c: concise version.
"""
class Solution1c:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            return max([dfs(j) for j in subord[i]] or []) + informTime[i]

        subord = collections.defaultdict(list)

        for i, mgr in enumerate(manager): # Not used: mgr[-1] = headID
            subord[mgr].append(i)

        return dfs(headID)

"""
Solution 1d: 
"""
class Solution1d:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            mx = 0

            for j in subord[i]:
                dfs_j = dfs(j)
                if dfs_j > mx:
                    mx = dfs_j
                #mx = max(mx, dfs(j))

            return mx + informTime[i]

        subord = collections.defaultdict(list)
        
        for i, mgr in enumerate(manager): # Not used: mgr[-1] = headID
            subord[mgr].append(i)

        return dfs(headID)

###############################################################################
"""
Solution 2: naive.

Very slow. TLE if use max().

Runtime: 7052 ms, faster than 10.00% of Python3 online submissions
Memory Usage: 28.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mx = 0
        
        for i in range(n):
            if informTime[i] == 0:
                total_time = 0

                while manager[i] != -1:
                    total_time += informTime[manager[i]]
                    i = manager[i]
                    
                #mx = max(mx, total_time)
                if total_time > mx:
                    mx = total_time
                
        return mx

###############################################################################
"""
Solution 3: improved naive.

Runtime: 1320 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 34.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mx = 0
        time = {headID: 0} #informTime[headID]}
        
        for i in range(n):
            if informTime[i] == 0:
                total_time = 0
                path = []

                while manager[i] != -1:
                    path.append(i)

                    if i in time:
                        total_time += time[i]
                        break

                    total_time += informTime[manager[i]]
                    
                    i = manager[i]

                ###
                # print()
                # print(f"path = {path}")
                # print(f"time = {time}")

                if path:
                    t = time[manager[path[-1]]]
                    for p in reversed(path):
                        t += informTime[manager[p]]

                        #if p not in time: 
                        time[p] = t

                if total_time > mx:
                    mx = total_time
                
        return mx

###############################################################################

if __name__ == "__main__":
    def test(n, headID, manager, informTime, comment):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}\n")
        print(f"\nhead ID = {headID}\n")
        print(f"\nmanager = {manager}\n")
        print(f"\ninform time = {informTime}\n")

        res = sol.numOfMinutes(n, headID, manager, informTime)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution1b()
    #sol = Solution1c()
    #sol = Solution1d()
    
    #sol = Solution2() # naive
    #sol = Solution3() # improved naive

    comment = "LC ex1; answer = 0"
    n = 1
    headID = 0
    manager = [-1]
    informTime = [0]
    test(n, headID, manager, informTime, comment)

    comment = "LC ex2; answer = 1"
    n = 6
    headID = 2
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]
    test(n, headID, manager, informTime, comment)

    comment = "LC ex3; answer = 21"
    n = 7
    headID = 6
    manager = [1,2,3,4,5,6,-1]
    informTime = [0,6,5,4,3,2,1]
    test(n, headID, manager, informTime, comment)

    comment = "LC ex4; answer = 3"
    n = 15
    headID = 0
    manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    test(n, headID, manager, informTime, comment)

    comment = "LC ex4; answer = 1076"
    n = 4
    headID = 2
    manager = [3,3,-1,2]
    informTime = [0,0,162,914]
    test(n, headID, manager, informTime, comment)

    comment = "LC test case; answer = 3665"
    n = 10
    headID = 3
    manager = [8,9,8,-1,7,1,2,0,3,0]
    informTime = [224,943,160,909,0,0,0,643,867,722]
    test(n, headID, manager, informTime, comment)
