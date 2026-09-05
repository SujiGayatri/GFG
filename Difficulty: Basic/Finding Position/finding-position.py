class Solution:
    def nthPosition (self, n):
        # code here 
        return 1 << (n.bit_length() - 1)