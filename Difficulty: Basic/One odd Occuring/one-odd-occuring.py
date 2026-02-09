from collections import Counter
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        fre=Counter(arr)
        for item,count in fre.items():
            if count%2!=0:
                return item