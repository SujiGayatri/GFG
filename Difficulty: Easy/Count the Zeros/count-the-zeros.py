#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code here
        cnt=0
        for i in arr:
            if i==0:
                cnt+=1
        return cnt