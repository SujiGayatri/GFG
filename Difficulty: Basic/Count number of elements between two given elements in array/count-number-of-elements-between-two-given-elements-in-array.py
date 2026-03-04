class Solution:
    def getCount(self, arr, num1, num2):
        #Your code goes here
        left = -1
        right = -1
        n = len(arr)
        for i in range(n):
            if arr[i] == num1:
                left = i
                break
        for i in range(n-1, -1, -1):
            if arr[i] == num2:
                right = i
                break
        if left == -1 or right == -1 or left >= right:
            return 0
        return right-left-1