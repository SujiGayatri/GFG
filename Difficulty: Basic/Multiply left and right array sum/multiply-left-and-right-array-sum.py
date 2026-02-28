#User function Template for python3

class Solution:
    def multiply(self, arr):
        # Code here
        n=len(arr)
        mid = n // 2
        left_s=0
        right_s=0
        for i in range(mid):
            left_s+=arr[i]
        for i in range(mid,n):
            right_s+=arr[i]
        return left_s*right_s