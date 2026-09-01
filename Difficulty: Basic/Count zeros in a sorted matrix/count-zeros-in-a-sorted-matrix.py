class Solution:
    def countZeros(self, mat):
        # code here
        n = len(mat)
        row = 0
        col = n - 1
        count = 0
        while row < n and col >= 0:
            if mat[row][col] == 0:
                count += col + 1
                row += 1
            else:
                col -= 1
        return count