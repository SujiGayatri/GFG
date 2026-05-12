#User function Template for python3

class Solution:
    
    def KthMissingElement(self,arr,k) : 
        #Complete the function
        n = len(arr)
        for i in range(1, n):
            missing = arr[i] - arr[i - 1] - 1
            if k <= missing:
                return arr[i - 1] + k
            k -= missing
        return -1