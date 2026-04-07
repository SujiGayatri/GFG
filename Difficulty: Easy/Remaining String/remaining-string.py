#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		index = -1
        occurrence = 0
        for i in range(len(s)):
            if s[i] == ch:
                occurrence += 1
                if occurrence == count:
                    index = i
                    break
        if index == -1:
            return ""
        elif index == len(s) - 1:
            return ""
        else:
            return s[index + 1:]