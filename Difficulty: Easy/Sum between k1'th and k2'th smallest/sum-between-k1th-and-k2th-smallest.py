class Solution:
    def sumBetweenK1K2(self, arr, k1, k2):
        # code here
        arr.sort()
        return sum(arr[k1:k2-1])