class Solution:
    def findMinSum(self, a, b):
        # code here
        a.sort()
        b.sort()
        ans = 0
        for i in range(len(a)):
            ans += abs(a[i] - b[i])
        return ans