class Solution:
    def nthRoot(self, n, m):
       # code here
       for i in range(m + 1):
           if i ** n == m:
               return i
       return -1
