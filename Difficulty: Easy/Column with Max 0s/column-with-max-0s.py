class Solution:
    def maxZeros(self, arr):
        # code here
        max_zeros = 0
        ans = -1
        for c in range(len(arr)):
            zero_count = 0
            for row in range(len(arr)):
                if arr[row][c] == 0:
                    zero_count += 1
            if zero_count > max_zeros:
                max_zeros = zero_count
                ans = c
        return ans