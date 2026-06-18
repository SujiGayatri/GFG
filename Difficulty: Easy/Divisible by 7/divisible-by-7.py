#User function Template for python3

class Solution:
    def isdivisible7(self, num):
        # code here
        rem = 0
        for digit in num:
            rem = (rem * 10 + int(digit)) % 7
        return 1 if rem == 0 else 0