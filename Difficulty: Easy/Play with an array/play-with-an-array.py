class Solution:
    def formatArray(self, arr):
        #code here
        arr.sort()
        n = len(arr)
        k = n // 2
        for i in range(k):
            if arr[i] >= arr[i + k]:
                return False
        return True