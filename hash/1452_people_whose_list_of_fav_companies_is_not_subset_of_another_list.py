"""
1452. People Whose List of Favorite Companies Is Not a Subset of Another List
Medium

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].

Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1] 
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].

Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]

Constraints:

    1 <= favoriteCompanies.length <= 100
    1 <= favoriteCompanies[i].length <= 500
    1 <= favoriteCompanies[i][j].length <= 20
    All strings in favoriteCompanies[i] are distinct.
    All lists of favorite companies are distinct, that is, If we sort alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
    All strings consist of lowercase English letters only.
"""

from typing import List

###############################################################################
"""
Solution: use set.

O(m * n^2) overall time, where n = length of input list, and m = max length of each sublist.
- O(n^2) factor for nested loops
- O(m) factor for checking if subset.

O(n) extra space: for output list
"""
class Solution:
    #def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        n = len(f)

        g = set(i for i in range(n)) 

        for i in range(n):
            curr = set(f[i])

            for j in range(n):
                if i == j or len(f[i]) > len(f[j]):
                    continue

                if curr.issubset(f[j]):
                    g.discard(i)
                    break

        return list(g)

###############################################################################
"""
Solution 2: same, but first convert input list to list of sets.

Also, don't use "g" set for result.

O(m * n^2) overall time, where n = length of input list, and m = max length of each sublist.
- O(n^2) factor for nested loops
- O(m) factor for checking if subset.

O(m * n) time to create "s".

O(m * n) extra space: for "s".
"""
class Solution2:
    #def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        n = len(f)

        res = []
        s = [set(fav) for fav in f]
        
        for i in range(n):
            curr = s[i]
            is_subset = True

            for j in range(n):
                #if i == j or len(curr) > len(s[j]):
                if i == j:
                    continue

                #if curr.issubset(s[j]):
                if curr <= s[j]:
                    is_subset = False
                    break
            
            if is_subset:
                res.append(i)

        return res

###############################################################################
"""
Solution 3: same, but use "not any()"
"""
class Solution3:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        n = len(f)

        res = []
        s = [set(fav) for fav in f]
        
        for i in range(n):
            curr = s[i]

            if not any(curr <= s[j] for j in range(n) if i != j):
                res.append(i)

        return res

"""
Solution 4: same, but more concise.
"""
class Solution4:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        s = [set(fav) for fav in f]

        return [i for i, curr in enumerate(s) 
            if not any(curr <= s[j] for j in range(n) if i != j)]

###############################################################################
"""
Solution 5: same as sol 1, but first sort "s" by length.
"""
class Solution5:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        n = len(f)

        g = set(range(n)) 
        
        s = [(set(fav), i) for i, fav in enumerate(f)]
        s.sort(key=lambda x: len(x[0]))

        for i in range(n):
            curr, idx = s[i]

            for j in range(i+1, n):
                #if curr.issubset(s[j][0]):
                if curr <= s[j][0]:
                    g.discard(idx)
                    break

        return list(g)
