#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        ans = ""
        curr = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                curr=s[i]+curr
            else:
                ans+=curr
                ans+=s[i]
                curr=""
        ans+=curr
        return ans