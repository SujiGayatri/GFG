#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # code here
        total = 0
        for i in arr:
            total += (i + k - 1) // k
        return total