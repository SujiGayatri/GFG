class Solution:

    def colSum(self, mat):
        # Code here
        n = len(mat)
        m = len(mat[0])
        ans = [0] * m
        for i in range(n):
            for j in range(m):
                ans[j] += mat[i][j]
        return ans