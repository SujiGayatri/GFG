class Solution:
    def median(self, arr):
        # code here
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) // 2
    
    def mean(self, arr):
        # code herearr.sort()
        return sum(arr) // len(arr)