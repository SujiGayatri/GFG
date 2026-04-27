#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        max_steps = 0
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                cnt += 1
                max_steps = max(max_steps, cnt)
            else:
                cnt = 0
        return max_steps