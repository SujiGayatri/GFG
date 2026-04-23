#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        i = 0  
        j = 0  
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                i += 1
            j += 1
        return i == len(A)