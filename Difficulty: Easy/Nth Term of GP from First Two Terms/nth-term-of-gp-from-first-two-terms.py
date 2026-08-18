import math
class Solution:
    def termOfGP(self, a, b, n):
        # code here
        if n == 1:
            return a
        r = b / a
        return math.floor(a * (r ** (n - 1)))