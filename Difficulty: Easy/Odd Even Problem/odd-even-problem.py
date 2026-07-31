from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        freq = Counter(s)
        count = 0
        for ch, f in freq.items():
            pos = ord(ch) - ord('a') + 1  
            if pos % 2 == 0 and f % 2 == 0:
                count += 1
            elif pos % 2 == 1 and f % 2 == 1:
                count += 1
        return "EVEN" if count % 2 == 0 else "ODD"