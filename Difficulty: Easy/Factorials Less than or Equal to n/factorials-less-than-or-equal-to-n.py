class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	result = []
        fact = 1
        i = 1
        while fact <= n:
            result.append(fact)
            i += 1
            fact *= i
        return result