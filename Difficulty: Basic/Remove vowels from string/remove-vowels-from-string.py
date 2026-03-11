#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		vowels = "aeiou"
        res = ""
        for char in s:
            if char not in vowels:
                res += char
        return res