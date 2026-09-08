from math import gcd
class Solution:
    def getSmallestDivNum(self, n): 
        # code here 
        lcm = 1
        for i in range(1, n + 1):
            lcm = lcm * i // gcd(lcm, i)
        return lcm