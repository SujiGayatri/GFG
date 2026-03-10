# You are required to complete this fucntion
# Function should return the an integer
class Solution:
    def findMaxProduct(self, arr, k):
        #code here
        n = len(arr)
        prod = 1
        for i in range(k):
            prod *= arr[i]
        max_prod = prod
        for i in range(k, n):
            prod = (prod // arr[i-k]) * arr[i]
            max_prod = max(max_prod, prod)
        return max_prod