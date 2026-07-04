class Solution:
    def areElementsContiguous (self, arr): 
    #Complete the function
        unique = set(arr)
        return max(unique) - min(unique) + 1 == len(unique)