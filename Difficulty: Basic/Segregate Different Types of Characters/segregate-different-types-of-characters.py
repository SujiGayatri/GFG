class Solution:
    def splitString(self, s): 
        # code here 
        letters = []
        digits = []
        special = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            elif ch.isdigit():
                digits.append(ch)
            else:
                special.append(ch)
        s1 = ''.join(letters) if letters else "-1"
        s2 = ''.join(digits) if digits else "-1"
        s3 = ''.join(special) if special else "-1"
        return [s1, s2, s3]