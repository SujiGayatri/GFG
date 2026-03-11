#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        set1 = set(s1)
        set2 = set(s2)
        unique_c = (set1 - set2) | (set2 - set1)
        sorted_unique_chars = sorted(list(unique_c))
        return "".join(sorted_unique_chars)