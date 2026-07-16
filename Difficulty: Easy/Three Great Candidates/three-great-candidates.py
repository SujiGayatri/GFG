class Solution:
    def maxProduct(self, arr):
        # code here
        arr.sort()
        n = len(arr)
        p1 = arr[n - 1] * arr[n - 2] * arr[n - 3]
        p2 = arr[0] * arr[1] * arr[n - 1]

        return max(p1, p2)