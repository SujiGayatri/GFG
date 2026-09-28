class Solution:
    def sandwichedVowel(self, s):
        # code here
        vowels = "aeiou"
        result = []

        for i in range(len(s)):
            if (i > 0 and i < len(s) - 1
                and s[i] in vowels
                    and s[i - 1] not in vowels
                    and s[i + 1] not in vowels):
                continue
            result.append(s[i])
        return ''.join(result)