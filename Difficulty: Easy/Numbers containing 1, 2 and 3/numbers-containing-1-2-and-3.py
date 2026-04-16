class Solution:
    def filterByDigits(self, arr):
        #code here
        result = []
        for i in arr:
            valid = True
            temp = i
            while temp > 0:
                digit = temp % 10
                if digit not in (1, 2, 3):
                    valid = False
                    break
                temp //= 10
            if valid:
                result.append(i)
        return result if result else [-1]