# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        n=str(n)
        n=n.replace('0','5')
        return int(n)