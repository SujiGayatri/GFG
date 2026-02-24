#User function Template for python3



class Solution:
    def arranged(self,arr):
        #Code here
        positives = []
        negatives = []
        for num in arr:
            if num >= 0:
                positives.append(num)
            else:
                negatives.append(num)
        res = []
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res