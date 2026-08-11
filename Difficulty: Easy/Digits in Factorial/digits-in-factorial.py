class Solution:
    def digitsInFactorial(self,n):
        # code here
        if n < 0:
            return 0
        if n <= 1:
            return 1
        x = (n * math.log10(n / math.e) + 
         0.5 * math.log10(2 * math.pi * n))
        return math.floor(x) + 1