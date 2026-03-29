#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        total_sum = 0
        for i in arr:
            while i > 0:
                total_sum += i % 10
                i //= 10
        return 1 if total_sum % 3 == 0 else 0