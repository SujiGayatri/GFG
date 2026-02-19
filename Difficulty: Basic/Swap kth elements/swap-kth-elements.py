
class Solution:
    def swapKth(self, arr, k):
        # Code Here
        n = len(arr)
        left = k - 1
        right = n - k
        arr[left], arr[right] = arr[right], arr[left]
        return arr