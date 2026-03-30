#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
	    s = str(n) + str(2*n) + str(3*n)
        return len(s) == 9 and sorted(s) == list("123456789")