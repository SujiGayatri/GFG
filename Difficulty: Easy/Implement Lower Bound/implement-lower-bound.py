class Solution:
    def lowerBound(self, arr, target):
        # code here
        l, high = 0, len(arr)
        while l < high:
            mid = (l + high) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                high = mid
        return l
        