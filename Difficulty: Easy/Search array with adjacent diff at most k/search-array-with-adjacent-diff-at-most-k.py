#User function Template for python3

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        # code here
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == x:
                return i
            j = max(1, abs(arr[i] - x) // k)
            i += j
        return -1