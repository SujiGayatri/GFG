class Solution:
    def getLastDigit(self, a, b):
        # code here
        if b == "0":
            return 1

        last = int(a[-1])
        b_mod_4 = 0
        for digit in b:
            b_mod_4 = (b_mod_4 * 10 + int(digit)) % 4
        exponent = b_mod_4 if b_mod_4 != 0 else 4

        return pow(last, exponent, 10)