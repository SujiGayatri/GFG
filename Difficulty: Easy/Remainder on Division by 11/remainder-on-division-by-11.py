class Solution:
    def remainder(self, s: str) -> int:
        # code here 
        rem = 0
        for digit in s:
            rem = (rem * 10 + int(digit)) % 11
        return rem