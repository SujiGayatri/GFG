class Solution:
    def segregateElements(self, arr):
        # code here
        n = len(arr)
        temp = []
        for i in range(n):
            if arr[i] >= 0:
                temp.append(arr[i])
        for i in range(n):
            if arr[i] < 0:
                temp.append(arr[i])
        for i in range(n):
            arr[i] = temp[i]