from bisect import bisect_left, bisect_right
class Solution:
    def isMajority(self, arr):
        # code here
        n = len(arr)
        candidate = arr[n // 2]
        left = bisect_left(arr, candidate)
        right = bisect_right(arr, candidate)
        count = right - left
        return count > n // 2