"""
1410. HTML Entity Parser
Medium

HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

Example 1:

Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The parser will replace the &amp; entity by &

Example 2:

Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""

Example 3:

Input: text = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"

Example 4:

Input: text = "x &gt; y &amp;&amp; x &lt; y is always false"
Output: "x > y && x < y is always false"

Example 5:

Input: text = "leetcode.com&frasl;problemset&frasl;all"
Output: "leetcode.com/problemset/all"

Constraints:

1 <= text.length <= 10^5
The string may contain any possible characters out of all the 256 ASCII characters.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use string.replace(old, new).
Assume we don't replace recursively.

O(n) time
O(n) extra space
"""
class Solution:
    def entityParser(self, text: str) -> str:
        d = {
            '&quot;': '"',
            '&apos;': '\'',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
            '&amp;': '&', # put at end to avoid replacing more than one level
        }

        for k, v in d.items():
            text = text.replace(k, v)

        return text

###############################################################################
"""
Solution: don't use built-in or library functions.
Assume we don't replace recursively.

O(n) time
O(n) extra space
"""
class Solution2:
    def entityParser(self, text: str) -> str:
        d = {
            '&amp;': '&',
            '&quot;': '"',
            '&apos;': '\'',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }

        res = []
        key = []
        i = 0
        n = len(text)

        while i < n:
            if text[i] == "&":
                key = ["&"]
                i += 1

                while i < n:
                    if text[i] == "&":
                        res.extend(key)
                        key = ["&"]
                        i += 1
                        continue

                    key.append(text[i])
                    
                    if text[i] == ";":
                        k = ''.join(key)
                        key = []

                        # if k in d:
                        #     res.append(d[k])
                        # else:
                        #     res.append(k)

                        res.append(d.get(k, k))
                        break
                    
                    i += 1

            else:
                res.append(text[i])

            i += 1

        if key:
            res.extend(key)

        return ''.join(res)

###############################################################################
"""
Solution 3: loop char by char, and use replace_mode boolean.
Assume we don't replace recursively.
"""
class Solution3:
    def entityParser(self, text: str) -> str:
        d = {
            '&amp;': '&',
            '&quot;': '"',
            '&apos;': '\'',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }

        res = []
        replace_mode = False

        for ch in text:
            if ch == "&":
                replace_mode = True
                key = ["&"]
            elif replace_mode:
                key.append(ch)
                if ch == ";":
                    k = ''.join(key)
                    res.append(d.get(k, k))
                    replace_mode = False
            else:
                res.append(ch)

        # if no keyword found after last "&"
        if replace_mode:
            res.extend(key)

        return ''.join(res)

###############################################################################
"""
Solution 4: when "&" is found, check substrings of matching length to each
keyword. Assume we don't replace recursively.
"""
class Solution4:
    def entityParser(self, text: str) -> str:
        d = {
            '&amp;': '&',
            '&quot;': '"',
            '&apos;': '\'',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }

        n = len(text)
        res = []
        i = 0

        while i < n:
            if text[i] == "&":
                for k, v in d.items():
                    if text[i:i+len(k)] == k:
                        res.append(v)
                        i += len(k)
                        break
                else:
                    res.append("&")
                    i += 1
            else:
                res.append(text[i])
                i += 1

        return ''.join(res)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")

        res = sol.entityParser(s)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution2()
    sol = Solution3()
    sol = Solution4()

    comment = "LC ex1; answer = & is an HTML entity but &ambassador; is not."
    s = "&amp; is an HTML entity but &ambassador; is not."
    test(s, comment)

    comment = 'LC ex2; answer = "and I quote: "..."'
    s = "and I quote: &quot;...&quot;"
    test(s, comment)

    comment = "LC ex3; answer = Stay home! Practice on Leetcode :)"
    s = "Stay home! Practice on Leetcode :)"
    test(s, comment)

    comment = "LC ex4; answer = x > y && x < y is always false"
    s = "x &gt; y &amp;&amp; x &lt; y is always false"
    test(s, comment)

    comment = "LC ex5; answer = leetcode.com/problemset/all"
    s = "leetcode.com&frasl;problemset&frasl;all"
    test(s, comment)
    
    comment = ""
    s = "&amp;gt;"
    test(s, comment)

    comment = ""
    s = "&amp;quot;"
    test(s, comment)
    
    comment = ""
    s = "&amp;amp;amp;"
    test(s, comment)

    comment = ""
    s = "harry & sally"
    test(s, comment)
