class Solution:
    def ExtractNumber(self,sentence):
        #code here
        max_num = -1
        for i in sentence.split():
            if i.isdigit() and '9' not in i:
                num = int(i)
                max_num = max(max_num, num)
        return max_num