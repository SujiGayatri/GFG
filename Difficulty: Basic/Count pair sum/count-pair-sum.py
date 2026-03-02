#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        i = 0
        j = len(arr2) - 1
        cnt = 0
        while i < len(arr1) and j >= 0:
            current_sum = arr1[i] + arr2[j]
            if current_sum == x:
                cnt += 1
                i += 1
                j -= 1
            elif current_sum < x:
                i += 1
            else:
                j -= 1
                
        return cnt