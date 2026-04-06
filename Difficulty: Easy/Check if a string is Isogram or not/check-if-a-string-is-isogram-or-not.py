class Solution:
    def isIsogram(self,s):
        #Your code here
        seen = set()
        for i in s:
            if i in seen:
                return False
            seen.add(i)
        return True