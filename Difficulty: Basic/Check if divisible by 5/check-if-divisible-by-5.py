class Solution:
    def divisibleBy5(self, n):
        # code here
        return n[-1] == '0' or n[-1] == '5'