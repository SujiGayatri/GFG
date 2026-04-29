class Solution:
    def minFlips(self, s):
        # Code here
        flips_start_0 = 0 
        flips_start_1 = 0  
        for i, c in enumerate(s):
            expected_0 = '0' if i % 2 == 0 else '1'
            expected_1 = '1' if i % 2 == 0 else '0'
            if c != expected_0:
                flips_start_0 += 1
            if c != expected_1:
                flips_start_1 += 1
        return min(flips_start_0, flips_start_1)
        
