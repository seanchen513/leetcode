"""
1472. Design Browser History
Medium

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

Constraints:

    1 <= homepage.length <= 20
    1 <= url.length <= 20
    1 <= steps <= 100
    homepage and url consist of  '.' or lower case English letters.
    At most 5000 calls will be made to visit, back, and forward.

"""

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

###############################################################################
"""
Solution: use list.

To avoid having to resize the history list in visit(), we add a variable
to track the effective max index of the history list. This also affects
forward().

O(1) time for each method

O(n) space, where n = number of URLs for which visit() is called
- actual space used might be much less if the total number of back steps
is large enough.
"""
class BrowserHistory:
    def __init__(self, homepage: str):
        self.h = [homepage] # history list of URLs
        self.i = 0 # index of current page with history list
        self.max_i = 0

    def visit(self, url: str) -> None:
        self.i += 1 # new index of where to put input url

        if self.i == len(self.h):
            self.h.append(url)
        else:
            self.h[self.i] = url

        self.max_i = self.i

    def back(self, steps: int) -> str:
        ### can move back at most self.i steps

        # if steps > self.i:
        #     steps = self.i
        # self.i -= steps

        self. i = max(0, self.i - steps)

        return self.h[self.i]

    def forward(self, steps: int) -> str:
        ### can move forward at most ... steps

        #self.i = min(len(self.h) - 1, self.i + steps) # old
        self.i = min(self.max_i, self.i + steps)

        return self.h[self.i]

"""
LC example:

google
facebook
youtube
back 1: facebook
back 1: google
fwd 1: facebook
visit: linkedin -- clears youtube?
fwd 2:

"""

###############################################################################
"""
Solution: use (dynamic) list.

__init__(), back(), forward(): O(1) time
visit(): O(n) time due to having to resize history list

"""
class BrowserHistory:
    def __init__(self, homepage: str):
        self.h = [homepage] # history list of URLs
        self.i = 0 # index of current page with history list

    def visit(self, url: str) -> None:
        self.i += 1
        self.h = self.h[:self.i] + [url]

    def back(self, steps: int) -> str:
        ### can move back at most self.i steps
        # if steps > self.i:
        #     steps = self.i
        # self.i -= steps

        self. i = max(0, self.i - steps)

        return self.h[self.i]

    def forward(self, steps: int) -> str:
        ### can move forward at most ... steps
        # if steps > len(self.h) - 1 - self.i:
        #     steps = len(self.h) - 1 - self.i
        # self.i += steps

        self.i = min(len(self.h) - 1, self.i + steps)

        return self.h[self.i]

###############################################################################
"""
Solution: store 2 stacks, one each for forward history and back history.
Also store current URL.

__init__(): O(1) time
visit(): O(1) time
back(), forward(): O(steps) time

Slower than implementations using a history list.
"""
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = homepage
        self.h_forward = [] # stack for forward history
        self.h_back = [] # stack for back hsitory

    def visit(self, url: str) -> None:
        self.h_forward = [] # reset the forward history

        self.h_back.append(self.cur) # move current URL into back history
        self.cur = url

    def back(self, steps: int) -> str:
        # Move back page -> current page -> forward page.
        # Do this "step" number of times.
        while steps > 0 and self.h_back:
            self.h_forward.append(self.cur) # move current URL into forward history
            self.cur = self.h_back.pop() # set current page to back page
            steps -= 1

        return self.cur

    def forward(self, steps: int) -> str:
        # Move forward page -> current page -> back page.
        # Do this "step" number of times.
        while steps > 0 and self.h_forward:
            self.h_back.append(self.cur) # move current URL into back history
            self.cur = self.h_forward.pop() # set current page to forward page
            steps -= 1

        return self.cur
