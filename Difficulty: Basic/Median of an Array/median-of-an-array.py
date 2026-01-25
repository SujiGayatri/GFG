class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n=len(arr)
        if n%2!=0:
            return arr[n//2]
        else:
            a = arr[n // 2]
            b = arr[n // 2 - 1]
            s = a + b
            if s % 2 == 0:
                return s // 2       
            else:
                return s / 2        
