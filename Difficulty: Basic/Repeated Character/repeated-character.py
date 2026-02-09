#User function Template for python3
from collections import Counter
class Solution:
    def firstRep(self, s):
        # code here
        freq=Counter(s)
        for item,c in freq.items():
            if c>1:
                return item
                break
        return '#'
        