class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        MOD = 1000000007
        p=1
        for i in arr:
            p = (p * i) % MOD
        return p