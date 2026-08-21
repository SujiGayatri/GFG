class Solution:
    def mergeArrays(self, a, b):
        # code here
        merged=sorted(a+b)
        for i in range(len(a)):
            a[i]=merged[i]
        for j in range(len(b)):
            b[j]=merged[len(a)+j]
        