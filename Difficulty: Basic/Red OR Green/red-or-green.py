#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        #code here
        r = S.count('R')
        g = N - r
        return min(r, g)