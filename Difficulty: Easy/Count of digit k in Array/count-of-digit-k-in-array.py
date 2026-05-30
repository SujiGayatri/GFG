class Solution:
    def countDigitK(self, k, arr):
        # code here
        k = str(k)
        ans = 0
        for num in arr:
            ans += str(num).count(k)
        return ans