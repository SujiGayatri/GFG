#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        if s[0].isupper():
            return s.upper()
        else:
            return s.lower()