"""
1434. Number of Ways to Wear Different Hats to Each Other
Hard

There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.

Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats
(3,5), (5,3), (1,3) and (1,5)

Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.

Example 4:

Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
Output: 111
 
Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.
"""

from typing import List
import collections

###############################################################################
"""
Q4 asks to count maximal matchings in a bipartite N x 40 graph. 

It can be done with the following dp: dp[mask][n_hats] = count of matchings 
for people whose indices bits are set in mask, using only first n_hats hats. 

Then dp[mask][n_hats] can be computed as dp[mask][n_hats - 1] 
(the last hat is not used) plus the sum of dp[submask][n_hats - 1] taken over
all submasks of mask that lack exactly one set bit, meaning that the 
corresponding person wears the last hat.

ie, ...plus sum over dp[submask][n_hats - 1] taken over all submasks of mask 
where someone who prefers the current hat n_hats hasn't selected a hat yet.
"""

###############################################################################
"""
Solution: DP tabulation on (hat index, mask of selected people) using bits.
This version uses dict for "pref".

Contrast to the other way of doing it: 
(person index, list/tuple or mask of selected hats).

To avoid TLE, key is to assign hats to people rather than people to hats.
40^10 << 10^40.
#hats ^ #ppl << #ppl ^ #hats

State vars:
hat = hat numbers 1 to hat that have been considered (1-based index)
- current hat (index) is being considered; previous hat (indices) already assigned
mask = kth bit is set if person k has selected a hat (0-based index)
- aka chosen; people visited

dp[hat][mask] = num ways to assign first "hat" number of hats to the
people available.

https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/discuss/608599/Yeah-well.-Just-make-me-cry-during-the-interview-An-Optimised-Iterative-DP

Triple-nested loops:
    hat = 1 .. max_hat (up to 40)
    mask = 0 .. max_mask (up to 2^10 - 1 = 1023)
    p_ind = 0 .. n-1 (up to n=10)

O(max_hat * max_mask * n) time, where n = number of people
= O(max_hat * 2^n * n)
This inner value is 40 * 2^10 * 10 = 409,600 with LC constraints.

O(max_hat * max_mask) extra space: for dp table
= O(max_hat * 2^n) 
This inner value is 40 * 2^10 = 40,960 with LC constraints.
(not counting extra row for dummy hat value of 0)

Using dict for "pref":
Runtime: 360 ms, faster than 89.37% of Python3 online submissions
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions

"""
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats) # number of people
        max_mask = (1 << n) - 1 # all 1's; state where everyone (bits 0..n) have selected a hat

        mod = 10**9 + 7

        ###        
        pref = collections.defaultdict(list) # maps hat index to list of people indices
        max_hat = 0

        ### find all the people interested in each hat
        for i in range(n): # each person
            for h in hats[i]: # each hat for person i
                pref[h].append(i)
                if h > max_hat:
                    max_hat = h

        #print(pref)

        dp = [[0] * (max_mask + 1) for _ in range(max_hat + 1)]  # [hat][mask]
        dp[0][0] = 1 # base case: no hats, no people

        for hat in range(1, max_hat + 1):
            # if hat not in pref: # optional
            #     dp[hat] = dp[hat-1]
            #     continue

            for mask in range(max_mask + 1):
                # don't use this hat
                dp[hat][mask] += dp[hat-1][mask] % mod

                # use this hat on available people who prefer it

                for p_ind in pref[hat]: # for each person that prefers current hat

                    # states where current person has selected a hat
                    if mask & (1 << p_ind): 
                        # add number of ways from corresponding state where 
                        # hats 0 to hat-1 have been considered, and where current 
                        # person has not yet selected a hat
                        dp[hat][mask] += dp[hat-1][mask ^ (1 << p_ind)] % mod
            
            # if max_hat < 10:
            #     print(f"hat={hat}, dp[hat] = {dp[hat]}")

        return dp[max_hat][max_mask] % mod

"""
Solution 1b: same, but use list of lists for "pref".
"""
class Solution1b:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats) # number of people
        max_mask = (1 << n) - 1 # all 1's; state where everyone (bits 0..n) have selected a hat

        mod = 10**9 + 7
        # max_hat = 40
        max_hat = max(max(h) for h in hats)

        # hat 0 is dummy
        pref = [[] for _ in range(max_hat + 1)] # [hat #][person #]
        
        ### find all the people interested in 1 hat
        for i in range(n): # each person
            for h in hats[i]: # each hat for person i
                pref[h].append(i)

        ###        
        dp = [[0] * (max_mask + 1) for _ in range(max_hat + 1)]  # [hat][mask]

        # base case: no hats, no people
        dp[0][0] = 1

        for hat in range(1, max_hat + 1):
            for mask in range(max_mask + 1):
                # don't use this hat
                dp[hat][mask] += dp[hat-1][mask] % mod

                # use this hat on available people who prefer it

                for p_ind in pref[hat]: # for each person that prefers current hat

                    # states where current person has selected a hat
                    if mask & (1 << p_ind): 
                        # add number of ways from corresponding state where 
                        # hats 0 to hat-1 have been considered, and where current 
                        # person has not yet selected a hat
                        dp[hat][mask] += dp[hat-1][mask ^ (1 << p_ind)] % mod
            
        return dp[max_hat][max_mask] % mod

"""
LC ex1:
hats = [[3,4],[4,5],[5]]

n = 3 people
max_mask = (1 << 3) - 1 = 2^3 - 1 = 7 = 0b111
max_hat = 5

# pref is 5 * 3 matrix [hat #][person #]

pref dict: 

hat#    list of people (0-based index) preferring that hat #
1       []
2       []
3       [0]
4       [0,1]
5       [1,2]

dp is 6 * 8 matrix [hat # = 1..5 (0 dummy)] [mask # = 0..7]

        000     001     010     011     100     101     110     111
hat #   mask0   mask1   mask2   mask3   mask4   mask5   mask6   mask7
0       1       0       0       0       0       0       0       0
1       1       0       0       0       0       0       0       0
2       1       0       0       0       0       0       0       0
3       1       1       0       0       0       0       0       0

4       1       2       1       1       0       0       0       0
5       1       2       2       3       1       2       1       1

hat 3:
pref[3] = [0]
    ie, for hat 3, person 0 is the only person who prefers it
p_ind = 0

(1 << p_ind) = (1 << 0) = 1
    ie, person 0 is 0th bit, corresponding to value 1

p_ind   1 << p_ind
0       1 = 0b001
1       2 = 0b010
2       4 = 0b100


mask = 0..7
mask & (1 << p_ind) = mask & 1 equals 1 for mask = 1, 3, 5, 7
- checks for states where person 0 has selected a hat

dp[hat][mask] += dp[hat-1][mask ^ (1 << p_ind)] % mod

mask ^ (1 << p_ind) = mask ^ 1
- flips last bit of mask; all other bits the same
- ie, flips bit corresponding to person that prefers current hat
- ie, look at corresponding state where person has not selected a hat yet


"""

"""
Solution 1c: same as sol 1, but use 1d DP table.

Runtime: 288 ms, faster than 96.40% of Python3 online submissions
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1c:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats) # number of people
        n_masks = 1 << n
        # max_mask = (1 << n) - 1 
        # max mask is all 1's; state where everyone (bits 0..n) have selected a hat

        mod = 10**9 + 7

        ###        
        pref = collections.defaultdict(list) # maps hat index to list of people indices
        max_hat = 0

        ### find all the people interested in each hat
        for i in range(n): # each person
            for h in hats[i]: # each hat for person i
                pref[h].append(i)
                if h > max_hat:
                    max_hat = h

        dp = [0] * n_masks
        dp[0] = 1 # base case: no hats, no people

        for hat in range(1, max_hat + 1):
            # if hat not in pref: # optional
            #     continue

            # don't use this mask...
            dp0 = dp[:]

            for mask in range(n_masks):
                # use this hat on available people who prefer it

                for p_ind in pref[hat]: # for each person that prefers current hat

                    # states where current person has selected a hat
                    if mask & (1 << p_ind): 
                        # add number of ways from corresponding state where 
                        # hats 0 to hat-1 have been considered, and where current 
                        # person has not yet selected a hat
                        dp[mask] += dp0[mask ^ (1 << p_ind)] % mod

        return dp[-1] % mod

###############################################################################
"""
Solution 2: DP memo.

https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/discuss/608778/Java-Top-down-DP-%2B-Bitmask-Clean-code
https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/discuss/608695/Assign-hats-to-people-don't-assign-people-with-hats

Similar codechef problem, which doesn't constrain with preferences:
https://discuss.codechef.com/t/tshirts-editorial/6723

"""
class Solution2:
    def numberWays(self, hats: List[List[int]]) -> int:
        def rec(mask, hat):
            if mask == max_mask: # check if everyone got a hat (all bits set)
                return 1

            if hat > max_hat: # no more hats to process
                return 0

            if dp[mask][hat] != -1: # memo
                return dp[mask][hat]

            ans = rec(mask, hat+1) # case when we don't assign hat to anyone
            
            # Case when we assign hat to someone:
            # We will assign the current hat to all possible persons we can,
            # and add to answer the respective number of ways.
            # Note that we are assigning distinct hats only, since current hat
            # has never been assigned before to anyone.
            
            #for p in range(n):
            for p in pref[hat]:
                if mask & (1 << p): # person p has already chosen a hat
                    continue
                
                # assign hat to person p
                ans = (ans + rec(mask | (1 << p), hat+1) ) % mod

            dp[mask][hat] = ans
            
            return ans


        mod = 10**9 + 7

        n = len(hats) # number of people
        max_mask = (1 << n) - 1
        max_hat = 40

        # build dict that maps each hat to a list of people that prefer it
        pref = collections.defaultdict(list)

        for i in range(n): # each person
            for h in hats[i]: # each hat that person i prefers
                pref[h].append(i)

        dp = [[-1] * (max_hat + 1) for _ in range(max_mask + 1)]
        
        return rec(0, 1)

"""
Solution 2b: same, but memoization is via functools.lru_cache() instead.
"""
import functools
class Solution2b:
    def numberWays(self, hats: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def rec(mask, hat):
            if mask == max_mask: # check if everyone got a hat (all bits set)
                return 1

            if hat > max_hat: # no more hats to process
                return 0

            ans = rec(mask, hat+1) # case when we don't assign hat to anyone
            
            # Case when we assign hat to someone:
            # We will assign the current hat to all possible persons we can,
            # and add to answer the respective number of ways.
            # Note that we are assigning distinct hats only, since current hat
            # has never been assigned before to anyone.
            
            #for p in range(n):
            for p in pref[hat]:
                if mask & (1 << p): # person p has already chosen a hat
                    continue
                
                # assign hat to person p
                ans = (ans + rec(mask | (1 << p), hat+1) ) % mod
            
            return ans

        mod = 10**9 + 7

        n = len(hats) # number of people
        max_mask = (1 << n) - 1
        max_hat = 40

        # build dict that maps each hat to a list of people that prefer it
        pref = collections.defaultdict(list) 

        for i in range(n): # each person
            for h in hats[i]: # each hat that person i prefers
                pref[h].append(i)
        
        return rec(0, 1)

###############################################################################
"""
Solution 3: DP memoized recursion on (person index, selected hats list/tuple).

Can use "selected" as a set, but won't be able to memoize since sets aren't
hashable. Can't use frozenset since we need to modify "selected".

Contrast to other approach that uses (hat index, list/tuple or mask of selected people).

TLE, but example to contrast vs sol 1.
This solution assigns 

"""
import functools
class Solution3:
    def numberWays(self, hats: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def rec(i, selected):
            if i == n-1:
                #return sum(1 for j in hats[-1] if j not in selected)
                return sum(1 for j in hats[-1] if selected[j] == 0)

                # count = 0
                # for j in hats[-1]:
                #     if selected[j] == 0: # if j not in selected:
                #         count += 1
                # return count
                    
            selected = list(selected)
            count = 0

            for j in hats[i]:
                if selected[j] == 0: # if j not in selected:
                    selected[j] = 1 # selected.add(j)
                    count += rec(i+1, tuple(selected)) # count += rec(i+1, selected)
                    selected[j] = 0 # selected.remove(j)

            return count % mod
        
        n = len(hats)                
        res = 0
        
        mod = 10**9 + 7
        selected = tuple([0] * 40) # selected = set()
        
        res = rec(0, selected)

        return res

###############################################################################
"""
Solution 4: use Mobius inversion formula

https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/discuss/611624/Clean-solution-using-Mobius-inversion-formula

"""
from itertools import chain, combinations
class Solution4:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats) # number of people
        
        mod = 10**9 + 7
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

        ### Construct dict d

        d = {} # maps combinations of people to how many hats they all prefer in common
        #hehe = list(chain.from_iterable(combinations(list(range(n)), r) for r in range(n+1)))
        combos = chain.from_iterable(combinations(list(range(n)), r) for r in range(n+1))
        
        for combo in combos:
            if len(combo) == 0:
                continue

            common = set.intersection(*[set(hats[person]) for person in combo])
            d[combo] = len(common)
        
        # print(f"\nsample combos = {list(d.keys())[:10]}")
        # print(f"numer of combos = len(d) = {len(d)}")

        ###

        def partition(collection):
            if len(collection) == 1:
                yield [ collection ]
                return

            first = collection[0]

            for smaller in partition(collection[1:]):
                # insert `first` in each of the subpartition's subsets
                for n, subset in enumerate(smaller):
                    yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
                
                # put `first` in its own subset 
                yield [ [ first ] ] + smaller

        ###

        everyone = list(range(n)) # list of all people
        count = 0

        # for n, p in enumerate(partition(everyone), 1):
        #     if n < 20:
        #         print(p)

        for n, p in enumerate(partition(everyone), 1):
            temp = 1

            for bl in p:
                ### Mobius inversion formula
                #temp = temp * ((-1)**(len(bl)-1)) * fac[len(bl)-1] * d[tuple(sorted(bl))]
                
                if len(bl) & 1: # odd; positive factor
                    temp *= fac[len(bl)-1] * d[tuple(sorted(bl))]
                else: # even; negative factor
                    temp *= -fac[len(bl)-1] * d[tuple(sorted(bl))]
                
                temp %= mod

            count = (count + temp) % mod

        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr={arr}")

        res = sol.numberWays(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # DP tabulation using bits
    #sol = Solution1b() # same, but use list of lists (instead of dict) for "pref"
    #sol = Solution1c() # same, but use 1d DP table

    #sol = Solution2() # DP recursion, memo
    #sol = Solution2b() # same, but use functools.lru_cache()

    #sol = Solution3() # TLE; DP memo on (person index, selected hats list/tuple)
    
    #sol = Solution4() # use Mobius inversion formula

    comment = "LC ex1; answer = 1"
    arr = [[3,4],[4,5],[5]]
    test(arr, comment)

    comment = "LC ex2; answer = 4"
    arr = [[3,5,1],[3,5]]
    test(arr, comment)

    comment = "LC ex3; answer = 24"
    arr = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    test(arr, comment)

    comment = "LC ex4; answer = 111"
    arr = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
    test(arr, comment)

    comment = "LC TC; answer = 778256459"
    arr = [[1,2,4,6,7,8,9,11,12,13,14,15,16,18,19,20,23,24,25],[2,5,16],[1,4,5,6,7,8,9,12,15,16,17,19,21,22,24,25],[1,3,6,8,11,12,13,16,17,19,20,22,24,25],[11,12,14,16,18,24],[2,3,4,5,7,8,13,14,15,17,18,21,24],[1,2,6,7,10,11,13,14,16,18,19,21,23],[1,3,6,7,8,9,10,11,12,14,15,16,18,20,21,22,23,24,25],[2,3,4,6,7,10,12,14,15,16,17,21,22,23,24,25]]
    test(arr, comment)

    comment = "LC TC; answer = 842465346"
    arr = [[1,3,5,10,12,13,14,15,16,18,19,20,21,27,34,35,38,39,40],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],[3,7,10,12,13,14,15,17,21,25,29,31,35,40],[2,3,7,8,9,11,12,14,15,16,17,18,19,20,22,24,25,28,29,32,33,34,35,36,38],[6,12,17,20,22,26,28,30,31,32,34,35],[1,4,6,7,12,13,14,15,21,22,27,28,30,31,32,35,37,38,40],[6,12,21,25,38],[1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40]]
    test(arr, comment)

    comment = "LC TC; answer = 178121190"
    arr = [[2,6,8,9,10,11,16,17,19,21,23,25],[1,3,6,7,8,9,10,11,12,13,14,19,20,22,23,25],[1,3,4,6,7,8,10,12,13,15,16,17,19,20,22],[2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,20,23,25],[1,4,5,8,12,14,15,16,19,22,24,25],[1,2,3,4,7,8,9,11,12,13,16,17,18,19,22,24,25],[1,2,3,4,10,12,14,17,18,20,21,22,23,24],[2,14,17,22]]
    test(arr, comment)
