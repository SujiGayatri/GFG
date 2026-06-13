#User function Template for python3

class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        pos = {arr[i]: i for i in range(n)}
        sorted_arr = sorted(arr)
        for i in range(n):
            if abs(pos[sorted_arr[i]] - i) > k:
                return "No"
        return "Yes"