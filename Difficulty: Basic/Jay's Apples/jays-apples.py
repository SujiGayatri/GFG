#User function Template for python3

class Solution:
    def minimumApple(self, arr):
        # Complete the function
        seen=set()
        for i in arr:
            if i not in seen:
                seen.add(i)
        l=list(seen)
        return len(l)