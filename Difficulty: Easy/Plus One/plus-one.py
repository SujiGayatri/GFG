#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        for i in range(N-1,-1,-1):
            if arr[i]<9:
                arr[i]+=1
                return arr
            arr[i] = 0
        return [1] + arr