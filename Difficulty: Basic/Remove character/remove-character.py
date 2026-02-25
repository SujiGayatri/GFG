#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        for i in str1:
            if i in str2:
                str1=str1.replace(i,"")
        return str1