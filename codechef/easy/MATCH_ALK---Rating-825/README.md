# MATCH_ALK - Rating 825

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Man of the Match

In a cricket match, there are two teams, each comprising $11$ players. The scorecard of the match lists the runs scored and wickets taken by each of these $22$ players.

To determine the "Man of the Match", we assess each player's performance. Points are awarded to a player as follows:

- Each run scored earns $1$ point.
- Every wicket taken earns $20$ points.

The player with the  **highest total points**  is awarded the "Man of the Match" title.

You are given the scorecard of a cricket match, listing the contributions of all $22$ players.
The players are numbered from $1$ to $22$. Find the "Man of the Match".
It is guaranteed that for all inputs to this problem, the "Man of the Match" is  **unique**.

 **Note** : A player who belongs to the losing team can also win the "Man of the Match" award.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $22$ lines of input. The $i$-th of these $22$ lines contains two space-separated integers $A_i$ and $B_i$ — respectively, the runs scored and wickets taken by the $i$-th player.
### Output Format

For each test case, output on a new line a single integer $i$ $(1 \leq i \leq 22)$ denoting the  *index*  of the player with the maximum score.

The tests for this problem are designed such that there will be exactly one player with the maximum score.

### Constraints
- $1 \leq T \leq 1000$
- $0 \leq A \leq 200$
- $0 \leq B \leq 10$
- There will be exactly $1$ player with the maximum score.
### Sample 1:
Input
Output

```
2
34 0
45 0
5 0
85 0
90 0
2 2
1 3
0 1
23 2
13 1
0 1
34 0
45 0
5 0
85 0
68 3
2 2
1 3
0 1
23 2
13 1
0 1
10 0
23 3
44 1
29 1
3 0
56 0
32 1
48 2
50 0
22 0
37 2
15 1
24 3
22 0
55 0
19 0
49 0
22 0
11 2
36 1
38 0
33 2
```

```
16
8

```

### Explanation:

 **Test case $1$:**  Player $16$ has $68$ runs and $3$ wickets, for a total of $68 + 3\times 20 = 128$ points.
It can be verified that this is the maximum score across all $22$ players.
Note that the output is $16$ (the index of the player) and not $128$ (the maximum score itself).

 **Test case $2$:**  Player $8$ scores the maximum points: $48 + 2 \times 20 = 88$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T16:25:24.781Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    max_points = -1
    answer = -1
    for i in range(1, 23):
        runs, wickets = map(int, input().split())
        points = runs + wickets * 20
        if points > max_points:
            max_points = points
            answer = i
    print(answer)
```

---

[View on CodeChef](https://www.codechef.com/problems/MATCH_ALK)