"""
1366. Rank Teams by Votes
Medium

In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.

Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 

Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.

Example 4:

Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation: 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.

Example 5:

Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.

Constraints:

1 <= votes.length <= 1000
1 <= votes[i].length <= 26
votes[i].length == votes[j].length for 0 <= i, j < votes.length.
votes[i][j] is an English upper-case letter.
All characters of votes[i] are unique.
All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.
"""

from typing import List
import collections
import functools

###############################################################################
"""
Solution: use sorting w/ custom key.

Use negative counts so teams with more votes come first when sorted.
Attach team letters at end of counts so that in case of ties, rank is
determined by alphabetical order of team letters.

O(nm log m) time: due to sorting
O(m^2) extra space: for "count" dict of lists

where n = num votes, m = num teams <= 26

Runtime: 68 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # ch = uppercase letter representing team
        count = {ch: [0] * len(votes[0]) + [ch] for ch in votes[0]} # O(nm)
        
        # O(nm) time total for nested loop
        for vote in votes:
            for pos, ch in enumerate(vote):
                count[ch][pos] -= 1

        return ''.join(sorted(votes[0], key=count.__getitem__))

###############################################################################
"""
Solution 2: use sorting.  Use custom comparator and convert it to key for 
sorted() using functools.cmp_to_key().

Runtime: 68 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution2:
    def rankTeams(self, votes: List[str]) -> str:
        n_teams = len(votes[0]) # number of teams or uppercase letters
        if n_teams == 1 or len(votes) == 1:
            return votes[0]

        # count[team][pos] = number of votes for team at rank pos = 1, ..., n_teams
        #count = {}
        count = collections.defaultdict(lambda: [0] * n_teams)

        for vote in votes:
            for pos, ch in enumerate(vote): # eg "ABCD"; team rep by ch
                #if ch not in rank:
                #    count[ch] = [0] * n_teams
                count[ch][pos] += 1

        def compare(ch1, ch2): # bigger ranks come first
            cnt1 = count[ch1] # eg, W: [1,0,0,1]
            cnt2 = count[ch2] # eg, X: [1,1,0,0]

            if cnt1 > cnt2: # then ch1 < ch2
                return -1
            elif cnt1 < cnt2: # then ch1 > ch2
                return 1
            else: # then rank alphabetically
                if ch1 < ch2:
                    return -1
                elif ch1 > ch2:
                    return 1
                else:
                    return 0

        return ''.join(sorted(votes[0], key=functools.cmp_to_key(compare)))

"""
LC example 2:
votes = ["WXYZ","XYZW"]

ranks:
W: [1,0,0,1]
X: [1,1,0,0]
Y: [0,1,1,0]
Z: [0,0,1,1]

W < X < Y < Z
"""

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.rankTeams(arr)

        print(f"\nres = {res}")


    sol = Solution() # use sorting
    sol = Solution2() # use sorting and custom comparator
    
    comment = "LC ex1; answer = ACB"
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    test(votes, comment)

    comment = "LC ex2; answer = XWYZ"
    votes = ["WXYZ","XYZW"]
    test(votes, comment)

    comment = "LC ex3; answer = ..."
    votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
    test(votes, comment)

    comment = "LC ex4; answer = ABC"
    votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
    test(votes, comment)

    comment = "LC ex5; answer = M"
    votes = ["M","M","M","M"]
    test(votes, comment)
