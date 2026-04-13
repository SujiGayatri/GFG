class Solution:
    def findClosestPair(self, arr1, arr2, x):
        #code here
        n = len(arr1)
        m = len(arr2)
        i = 0
        j = m - 1
        closest_diff = float('inf')
        res = (0, 0)
        while i < n and j >= 0:
            s = arr1[i] + arr2[j]
            diff = abs(s - x)
            if diff < closest_diff:
                closest_diff = diff
                res = (arr1[i], arr2[j])
            if s > x:
                j -= 1
            else:
                i += 1
        return list(res)