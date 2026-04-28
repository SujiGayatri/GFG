#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        n = len(arr)
        res = []
        i, j = 0, n - 1
        while i <= j:
            if i != j:
                res.append(arr[i])
                res.append(arr[j])
            else:
                res.append(arr[i])
            i += 1
            j -= 1
        total = 0
        for k in range(n):
            total += abs(res[k] - res[(k + 1) % n])
        return total