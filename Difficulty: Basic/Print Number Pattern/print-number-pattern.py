class Solution:
    def printPat(self, n):
        #write code here
        ans=[]
        for i in range(n,0,-1):
            for num in range(n,0,-1):
                ans.extend([num] * i)      
            ans.append(-1)               
        
        return ans