#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        stack = []
        for i in arr:
            if stack:
                top = stack[-1]
                if (top >= 0 and i < 0) or (top < 0 and i >= 0):
                    stack.pop() 
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack