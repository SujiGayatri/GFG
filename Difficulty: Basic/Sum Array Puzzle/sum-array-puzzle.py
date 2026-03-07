class Solution:
    def sumArray(self, arr):
        #Your Code goes here
        t = sum(arr)
        for i in range(len(arr)):
            arr[i] = t - arr[i]
        return arr