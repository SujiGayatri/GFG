class Solution:
    def find_unique(self, k, arr):
        #code here
        result = 0
        for bit in range(32):
            bit_sum = 0
            for i in arr:
                if i & (1 << bit):
                    bit_sum += 1
            if bit_sum % k != 0:
                result |= (1 << bit)
        
        return result