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