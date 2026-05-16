#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here 
        i = 0 
        j = 1  
        while i < N and j < N:
            if arr[i] % 2 == 0:
                i += 2
            elif arr[j] % 2 == 1:
                j += 2
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 2
                j += 2