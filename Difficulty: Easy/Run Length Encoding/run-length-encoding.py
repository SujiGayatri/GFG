class Solution:
    def encode(self, s : str) -> str:
        # code here
        encoded_s = ""
        if not s:
            return encoded_s
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                encoded_s += s[i-1] + str(count)
                count = 1
        encoded_s += s[-1] + str(count)
        return encoded_s