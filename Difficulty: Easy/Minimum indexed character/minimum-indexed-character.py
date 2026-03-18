class Solution:
    def minIndexChar(self,s1,s2): 
        #code here
        min_index = -1
        for i in range(len(s1)):
            if s1[i] in s2:
                if min_index==-1:
                    min_index=i
                else:
                    min_index=min(min_index, i)
        return min_index