class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        fou=set()
        for num in arr:
            if A <= num <= B:
                fou.add(num)
        
        return len(fou) == (B - A + 1)