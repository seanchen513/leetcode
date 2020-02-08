"""
277. Find the Celebrity
Medium

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:

Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:

Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
 
Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
def knows(a: int, b: int) -> bool:
    return adj[a][b]

###############################################################################
"""
Solution: traverse upper triangular region using staircase loop to find
only possible candidate for celebrity.  Then verify.

O(n) time: three O(n) loops (can combine two of them)
O(1) extra space
"""
class Solution:
    def findCelebrity(self, n: int) -> int:
        # Start with 0 as candidate for celebrity.
        # First row of adjacency matrix.
        x = 0

        # Looping horizontally through column numbers of adjacency matrix.
        # Traversing a staircase pattern within upper triangular region.
        for i in range(n):
            # If x knows someone, then x can't be celebrity, so move on
            # to the first known person as the new candidate.
            # Move on to row i of the adjacency matrix.
            # On next loop iteration, we start with row i, col i+1.
            if knows(x, i):
                x = i

        # x is now the only possible candidate for celebrity.
        # Suppose there was a celebrity y > x.  Then in y's column, there would
        # be all 1's.  Traversing along x's row would have hit the 1 in
        # column y.  But this means x knows y, so x cannot be a celebrity,
        # and our candidate would have been y instead.
        
        # Still need to verify that x is actually a celebrity.

        # Check that x doesn't know any i < x.
        # Ie, that row x is all 0's except for (x, x).
        # We already checked that knows(x, i) is 0 for i > x in the loop above.
        # Note the range is range(x), or 0, 1, ..., x-1.
        if any(knows(x, i) for i in range(x)):
            return -1 # x knows some i < x, so x can't be a celebrity

        # Check that everyone knows x, ie, that column x is all 1's.
        if any(not knows(i, x) for i in range(n)):
            return -1 

        return x

###############################################################################
"""
Celebrity's row is all zeros except at celebrity's index.
Celebrity's column is all ones.

O(n^2) time
O(n) extra space

TLE
"""
class Solution2:
    def findCelebrity(self, n: int) -> int:
        cand = []

        for j in range(1, n):
            if knows(0, j):
                cand += [j]

        if len(cand) == 0:
            cand = [0]

        cand2 = []
        for c in cand:
            if all(knows(i, c) for i in range(n)):
                cand2 += [c]

        if cand2 == [0]:
            return 0

        for c in cand2:
            if all(not knows(c,j) for j in range(c)) and all(not knows(c,j) for j in range(c+1,n)):
                return c

        return -1

###############################################################################
"""
O(n^2) time
O(n) extra space

TLE
"""
class Solution3:
    def findCelebrity(self, n: int) -> int:
        INF = float('inf')
        votes = [-1] + [0]*n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if knows(i, j):
                    votes[j] += 1
                    votes[i] = INF

        for i, v in enumerate(votes):
            if v == n - 1:
                return i

        return -1

###############################################################################

if __name__ == "__main__":
    def test(adj, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{adj}")
        
        res = s.findCelebrity(len(adj))

        print(f"\nresult = {res}")


    s = Solution() # O(n) sol
    #s = Solution2() # O(n^2) sol
    #s = Solution3() # O(n^2) sol

    comment = "LC ex1; answer = 1"
    adj = [[1,1,0],[0,1,0],[1,1,1]]
    test(adj, comment)

    comment = "LC ex2; answer = -1"
    adj = [[1,0,1],[1,1,0],[0,1,1]]
    test(adj, comment)

    comment = "LC test case; answer = -1"
    adj = [[1,1], [1,1]]
    test(adj, comment)
