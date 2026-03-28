#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,N,S):
        if S > 9 * N:
            return "-1"
        if S == 0:
            return "0"*N
        result = []
        for i in range(N):
            if S >= 9:
                result.append('9')
                S -= 9
            else:
                result.append(str(S))
                S = 0
        return "".join(result)