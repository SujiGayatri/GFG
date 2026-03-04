#User function Template for python3



class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        # code here
        res = []
        for i in arr:
            if i < k and i >= 10:
                temp = i
                prev = temp % 10
                temp //= 10
                valid = True
                
                while temp > 0:
                    curr = temp % 10
                    if abs(curr - prev) != 1:
                        valid = False
                        break
                    prev = curr
                    temp //= 10
                
                if valid:
                    res.append(i)
        return res