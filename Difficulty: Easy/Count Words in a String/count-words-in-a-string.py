class Solution:
    def countWords(self, s: str) -> int:
        # code here
        count = 0
        in_word = False
        for ch in s:
            if 'a' <= ch <= 'z':
                if not in_word:
                    count += 1
                    in_word = True
            else: 
                in_word = False
        return count