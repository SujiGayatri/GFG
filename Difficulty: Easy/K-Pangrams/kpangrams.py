class Solution:
    def kPangram(self,s, k):
    # code here
        letters = set()
        alpha_count = 0
        for ch in s:
            if 'a' <= ch <= 'z':
                letters.add(ch)
                alpha_count += 1
        if alpha_count < 26:
            return False
        missing = 26 - len(letters)
        return missing <= k