#User function Template for python3

class Solution:

    def countStr(self, n):
        # code here
        res = 0
        res += 1                          
        res += n                         
        res += n                          
        res += (n * (n - 1)) // 2        
        res += n * (n - 1)                
        res += (n * (n - 1) * (n - 2)) // 2  
        return res