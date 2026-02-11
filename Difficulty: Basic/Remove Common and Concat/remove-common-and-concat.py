class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        com = set(s1) & set(s2)
        result = []
        for ch in s1:
            if ch not in com:
                result.append(ch)
        for ch in s2:
            if ch not in com:
                result.append(ch)
        
        return "".join(result) if result else "-1"