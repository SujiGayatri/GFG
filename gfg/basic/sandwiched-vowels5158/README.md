# Remove Sandwiched Vowels

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given string  **s** containing only lowercase English alphabets, eliminate the vowels from the string that occur between two consonants (sandwiched between two immediately adjacent consonants). Return the new string.

 **Examples:** 

```
Input : s = "bab"
Output : bb
Explanation: 'a' is a vowel occuring between two consonants i.e. b. Hence the updated string eliminates a.
```

```
Input : s = "ceghij"
Output : cghj
Explanation: 'e' and 'i' are sandwitched vowels.
```

**Constraints:
**1 ≤ s.size() ≤ 106
'a' ≤ s[i] ≤ 'z'

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T16:18:43.184Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sandwiched-vowels5158/1)