class Solution:

    def modifyArray(self, arr):
        #code here
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] != -1 and arr[i] != i:
                correct_idx = arr[i]
                if arr[correct_idx] != arr[i]:
                    arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
                else:
                    arr[i] = -1
                    i += 1
            else:
                i += 1
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1
        return arr