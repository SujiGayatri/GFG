#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        # code here 
        steps = 0
        neg_count = 0
        zero_count = 0
        for x in arr:
            if x > 0:
                steps += (x - 1)
            elif x < 0:
                steps += (-1 - x)
                neg_count += 1
            else:
                steps += 1
                zero_count += 1
        if neg_count % 2 == 1 and zero_count == 0:
            steps += 2

        return steps