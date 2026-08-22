class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        digit_sum = sum(int(d) for d in str(n))
        return str(digit_sum) == str(digit_sum)[::-1]