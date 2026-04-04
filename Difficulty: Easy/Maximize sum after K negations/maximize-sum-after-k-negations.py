#User function Template for python3

class Solution:
    def maximizeSum(self, arr, n, k):
        # Your code goes here
        arr.sort(key=abs)
        for i in range(n - 1, -1, -1):
            if arr[i] < 0 and k > 0:
                arr[i] = -arr[i]
                k -= 1
        if k % 2 == 1:
            arr[0] = -arr[0]  
        return sum(arr)