# Maximum 69 Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a positive integer `num` consisting only of digits `6` and `9`.

Return  *the maximum number you can get by changing  **at most**  one digit (* `6` *becomes* `9` *, and* `9` *becomes* `6` *)*.

 

 **Example 1:** 

```
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

```

 **Example 2:** 

```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

```

 **Example 3:** 

```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

```

 

 **Constraints:** 

- 1 <= num <= 104
- num consists of only 6 and 9 digits.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.1 MB (beats 98.19%)  
**Submitted:** 2026-09-27T15:55:51.370Z  

```py
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        return int(''.join(s))
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-69-number/)