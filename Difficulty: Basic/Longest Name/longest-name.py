
class Solution:
    def longest(self, arr):
        # code here
        res=""
        for i in arr:
            if(len(i)>len(res)):
                res=i
        return res