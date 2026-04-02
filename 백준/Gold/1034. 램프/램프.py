from collections import defaultdict

N, M = map(int, input().split())
dt = defaultdict(int)
for _ in range(N):
    row = input()
    dt[row] += 1
K = int(input())

ans = 0
for key in dt.keys():
    if (cnt:=key.count('0')) % 2 == K%2 and cnt <= K:
        ans = max(ans, dt[key])
print(ans)