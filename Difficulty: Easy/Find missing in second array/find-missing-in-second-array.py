#User function Template for python3


class Solution:
    def findMissing(self,a,b):
    # code here
        b_set = set(b)  
        result = []
        for num in a:  
            if num not in b_set:
                result.append(num)
        return result