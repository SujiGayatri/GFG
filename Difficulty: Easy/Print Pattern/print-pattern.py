class Solution:
    def pattern(self, n):
        # code here
        ans = []
        def solve(x):
            ans.append(x)
            if x <= 0:
                return
            solve(x - 5)
            ans.append(x)
        solve(n)
        return ans