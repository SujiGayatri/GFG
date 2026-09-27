# The Lazy Caterer's Problem

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n**, denoting the number of cuts that can be made on a pancake, find the maximum number of pieces that can be formed by making n cuts.
 **Note:**  Cuts can't be horizontal.

 **Examples:** 

```
Input: n = 5
Output: 16
Explanation:  16 pieces can be formed by making 5 cuts.
 
```

```
Input: n = 3
Output: 7
Explanation: 7 pieces can be formed by  making 3 cuts.

```

 **Constraints:** 
1 ≤ n ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T15:56:36.909Z  

```py
class Solution:
    def maxCuts(self, n):
        # code here
        return (n * (n + 1)) // 2 + 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-lazy-caterers-problem2527/1)