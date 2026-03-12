#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		res = S[0]   
        for i in range(1, len(S)):
            if S[i] == " ":
                res += S[i+1]
        return res