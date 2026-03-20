class Solution:
    def findSum(self, s):
        #code here
        sum_n = 0
        current_number = ""
        for char in s:
            if char.isdigit():
                current_number += char
            else:
                if current_number:
                    sum_n += int(current_number)
                    current_number = ""
        if current_number:
            sum_n += int(current_number)
        return sum_n